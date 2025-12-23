import streamlit as st
import pandas as pd
import numpy as np
import io

from utils.aes_text import encrypt_text, decrypt_text
from utils.aes_image import encrypt_image
from utils.npcr_uaci import calculate_npcr, calculate_uaci

from utils.linear_approximation import linear_approximation_probability
from utils.nonlinearity import compute_nonlinearity
from utils.differential_uniformity import compute_differential_uniformity
from utils.avalanche_criterion import strict_avalanche_criterion
from utils.differential_approximation import calculate_dap
from utils.entropy import compute_entropy
from utils.bit_independence import calculate_bic_sac, calculate_bic_nl
from utils.algebraic_degree import compute_algebraic_degree
from utils.correlation_immunity import compute_correlation_immunity
from utils.transparency_order import compute_transparency_order


def main():
    st.title("S-box44 Cryptographic Evaluation & AES Encryption")
    st.header("Kelompok 13")
    st.text("Anggota kelompok:")
    st.text("Muhammad Syafiq Fadhilah (4611422033)")
    st.text("Melani Siyamafiroh (4611422141)")
    st.text("Livia Citra Atrianda (4611422142)")

    # SESSION STATE
    if "sbox" not in st.session_state:
        st.session_state.sbox = None

    # UPLOAD S-BOX
    st.header("Upload S-box")

    col1, col2, col3 = st.columns([1, 4, 1])
    with col2:
        uploaded_file = st.file_uploader(
            "Upload S-box (CSV / Excel, 256 values)",
            type=["csv", "xls", "xlsx"]
        )

    if uploaded_file:
        try:
            with st.spinner("Processing S-box..."):
                if uploaded_file.name.endswith(".csv"):
                    df = pd.read_csv(uploaded_file, header=None)
                else:
                    df = pd.read_excel(uploaded_file, header=None)

                sbox = df.values.flatten().astype(int).tolist()

                if len(sbox) < 256:
                    st.warning(f"S-box hanya {len(sbox)} elemen, dipadding ke 256.")
                    sbox.extend([0] * (256 - len(sbox)))
                elif len(sbox) > 256:
                    st.warning(f"S-box {len(sbox)} elemen, dipotong ke 256.")
                    sbox = sbox[:256]

                # SIMPAN DI SESSION STATE (PENTING)
                st.session_state.sbox = sbox

                st.success("S-box berhasil dimuat.")

        except Exception as e:
            st.error(f"Gagal memuat S-box: {e}")

    # TAMPILKAN & EVALUASI S-BOX
    if st.session_state.sbox is not None:
        st.divider()
        st.header("Imported S-box")

        sbox_grid = np.array(st.session_state.sbox).reshape(16, 16)
        st.table(pd.DataFrame(
            sbox_grid,
            columns=[str(i) for i in range(16)],
            index=[str(i) for i in range(16)]
        ))

        st.divider()
        st.header("S-box Cryptographic Evaluation")

        sbox = st.session_state.sbox

        st.metric("Nonlinearity", compute_nonlinearity(sbox))
        st.metric("SAC", f"{strict_avalanche_criterion(sbox):.10f}")
        st.metric("BIC-NL", calculate_bic_nl(sbox))
        st.metric("BIC-SAC", f"{calculate_bic_sac(sbox):.10f}")
        st.metric("LAP", f"{linear_approximation_probability(sbox):.6f}")
        st.metric("DAP", f"{calculate_dap(sbox):.10f}")
        st.metric("Algebraic Degree (AD)", compute_algebraic_degree(sbox))
        st.metric("Correlation Immunity (CI)", compute_correlation_immunity(sbox))
        st.metric("Transparency Order (TO)", f"{compute_transparency_order(sbox):.6f}")


        export_df = pd.DataFrame(sbox)
        buffer = io.BytesIO()
        export_df.to_excel(buffer, index=False, header=False)
        buffer.seek(0)

        st.download_button(
            "Download S-box",
            data=buffer,
            file_name="sbox.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

    # TEXT ENCRYPTION
    st.divider()
    st.header("AES Text Encryption")

    mode = st.radio("Mode", ["Encrypt", "Decrypt"], horizontal=True)
    text = st.text_area("Plaintext" if mode == "Encrypt" else "Ciphertext")
    key = st.text_input("Key (16 bytes)", type="password")

    if st.button(mode, key="btn_text"):
        if st.session_state.sbox is None:
            st.error("Silakan upload S-box terlebih dahulu.")
        elif len(key.encode()) != 16:
            st.error("Key harus 16 byte (AES-128).")
        else:
            if mode == "Encrypt":
                ciphertext = encrypt_text(text, key, st.session_state.sbox)
                entropy_result = compute_entropy(ciphertext.encode())
                entropy_value = entropy_result['shannon_entropy']
                
                st.subheader("Ciphertext")
                st.code(ciphertext)
                st.metric("Entropy", f"{entropy_value:.4f}")
            else:
                plaintext = decrypt_text(text, key)
                st.subheader("Plaintext")
                st.text(plaintext)

   # IMAGE ENCRYPTION
    st.divider()
    st.header("AES Image Encryption")
    
    img_mode = st.radio(
        "Mode",
        ["Encrypt", "Decrypt"],
        horizontal=True,
        key="img_mode"
    )
    
    uploaded_img = st.file_uploader(
        "Upload Image",
        type=["png", "jpg", "jpeg"]
    )
    
    img_key = st.text_input(
        "Image Key (16 bytes)",
        type="password",
        key="img_key"
    )
    
    if st.button(img_mode, key="btn_image"):
        if st.session_state.sbox is None:
            st.error("Silakan upload S-box terlebih dahulu.")
        elif uploaded_img is None:
            st.error("Silakan upload image terlebih dahulu.")
        elif len(img_key.encode()) != 16:
            st.error("Key harus 16 byte (AES-128).")
        else:
            from PIL import Image
    
            img = Image.open(uploaded_img).convert("RGB")
            img_np = np.array(img)
            key_bytes = img_key.encode().ljust(16, b"\0")[:16]
    
            if img_mode == "Encrypt":
                cipher1 = encrypt_image(img_np, key_bytes, st.session_state.sbox)
                cipher2 = encrypt_image(
                    img_np,
                    (img_key + "1").encode().ljust(16, b"\0")[:16],
                    st.session_state.sbox
                )
    
                entropy_res = compute_entropy(cipher1)
                npcr_res = calculate_npcr(cipher1, cipher2)
                uaci_res = calculate_uaci(cipher1, cipher2)
    
                entropy_val = entropy_res['shannon_entropy']
                npcr_val = npcr_res['npcr'] if isinstance(npcr_res, dict) else npcr_res
                uaci_val = uaci_res['uaci'] if isinstance(uaci_res, dict) else uaci_res
    
                st.subheader("Cipher Image")
                st.image(cipher1, clamp=True)
                st.caption(
                    "NPCR dan UACI dihitung dari dua cipher-image "
                    "dengan kunci berbeda"
                )
    
                col1, col2, col3 = st.columns(3)
                col1.metric("Entropy", f"{entropy_val:.4f}")
                col2.metric("NPCR (%)", f"{npcr_val:.2f}")
                col3.metric("UACI (%)", f"{uaci_val:.2f}")
    
            else:
                try:
                    from utils.aes_image import decrypt_image
                    plain_img = decrypt_image(
                        img_np,
                        key_bytes,
                        st.session_state.sbox
                    )
                    
                    st.subheader("Decrypted Image")
                    st.image(plain_img, clamp=True)
                except NotImplementedError:
                    st.warning(
                        "Fitur decrypt image belum diimplementasikan "
                        "di utils.aes_image."
                    )

if __name__ == "__main__":
    main()
