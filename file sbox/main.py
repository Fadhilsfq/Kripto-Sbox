import streamlit as st
import pandas as pd
import numpy as np
import io

# Import all the utility functions
from utils.linear_approximation import linear_approximation_probability
from utils.nonlinearity import compute_nonlinearity
from utils.differential_uniformity import compute_differential_uniformity
from utils.avalanche_criterion import strict_avalanche_criterion
from utils.differential_approximation import calculate_dap
from utils.entropy import compute_entropy
from utils.bit_independence import calculate_bic_sac, calculate_bic_nl

def main():
    st.title('S-box44 Cryptographic')

    # Layout to center the file uploader on the page
    col1, col2, col3 = st.columns([1, 4, 1])

    with col2:
        # File upload widget centered on the page
        uploaded_file = st.file_uploader(
            "Choose an Excel/CSV file", 
            type=['xlsx', 'xls', 'csv']
        )

    # Initialize session state for S-box
    if 'sbox' not in st.session_state:
        st.session_state.sbox = None

    try:
        # Read the uploaded file
        if uploaded_file is not None:
            # Add a loading spinner while processing the file
            with st.spinner('Processing the S-box...'):
                if uploaded_file.name.endswith('.csv'):
                    df = pd.read_csv(uploaded_file, header=None)
                elif uploaded_file.name.endswith(('.xls', '.xlsx')):
                    df = pd.read_excel(uploaded_file, header=None)
                else:
                    st.error("Invalid file type. Please upload a CSV or Excel file.")
                    return

                # Flatten the dataframe to a 1D list and convert to integers
                sbox = df.values.flatten().astype(int).tolist()

                # Validate and adjust S-box size
                if len(sbox) < 256:
                    st.warning(f"S-box size is {len(sbox)}. Padding to 256 elements.")
                    sbox.extend([0] * (256 - len(sbox)))  # Padding to 256
                elif len(sbox) > 256:
                    st.warning(f"S-box size is {len(sbox)}. Truncating to 256 elements.")
                    sbox = sbox[:256]  # Truncating to 256

                # Store S-box in session state
                st.session_state.sbox = sbox

                # Display S-box DataFrame  
                st.subheader('Imported S-box')  
                # Reshape the sbox into a 16x16 grid  
                sbox_grid = np.array(sbox).reshape(16, 16)  
                st.table(pd.DataFrame(sbox_grid,   
                                    columns=[f'{i}' for i in range(16)],   
                                    index=[f'{i}' for i in range(16)])  
                )  

                # Perform selected evaluations
                st.subheader('S-box44 Cryptographic Evaluation')

                # Nonlinearity
                nonlinearity = compute_nonlinearity(sbox)
                st.metric('Nonlinearity', str(nonlinearity))

                # Strict Avalanche Criterion  
                sac_value = strict_avalanche_criterion(sbox)  
                st.metric('Strict Avalanche Criterion (SAC)', f'{sac_value:.10f}')

                # BIC-NL  
                bic_nl_value = calculate_bic_nl(sbox)  
                st.metric('Bit Independence Criterion - Nonlinearity (BIC-NL)', str(bic_nl_value))

                # BIC-SAC  
                bic_sac_value = calculate_bic_sac(sbox)  
                st.metric('Bit Independence Criterion - SAC (BIC-SAC)', f'{bic_sac_value:.10f}')

                # Linear Approximation Probability
                lap_value = linear_approximation_probability(sbox)
                st.metric('Linear Approximation Probability (LAP)', f'{lap_value:.6f}')

                # Differential Approximation Probability  
                dap_value = calculate_dap(sbox)  
                st.metric('Differential Approximation Probability (DAP)', f'{dap_value:.10f}')

                # Export option
                export_df = pd.DataFrame(sbox)
                export_buffer = io.BytesIO()
                export_df.to_excel(export_buffer, index=False, header=False)
                export_buffer.seek(0)

                st.download_button(
                    label="Download S-box as Excel",
                    data=export_buffer,
                    file_name="sbox_data.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )

        else:
            st.info("Please upload an S-box file to continue.")
    
    except Exception as e:
        st.error(f"Error processing file: {str(e)}")

if __name__ == '__main__':
    main()