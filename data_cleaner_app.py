import streamlit as st
import pandas as pd

st.set_page_config(page_title="Salary & Exp Data Cleaner", layout="wide")

st.title("🧹 Salary & Experience Data Cleaner")
st.write(
    "Upload a CSV with `Salary` and `Exp` columns. "
    "This app strips non-numeric characters and converts both columns to integers."
)

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:
    clean_data = pd.read_csv(uploaded_file)

    st.subheader("Raw Data Preview")
    st.dataframe(clean_data.head(10))

    missing_cols = [c for c in ["Salary", "Exp"] if c not in clean_data.columns]
    if missing_cols:
        st.error(f"Missing expected column(s): {', '.join(missing_cols)}")
    else:
        # Clean Salary
        clean_data["Salary"] = (
            clean_data["Salary"]
            .astype(str)
            .str.replace(r"[^0-9]", "", regex=True)
        )
        clean_data["Salary"] = pd.to_numeric(
            clean_data["Salary"], errors="coerce"
        )

        # Clean Exp
        clean_data["Exp"] = (
            clean_data["Exp"]
            .astype(str)
            .str.replace(r"[^0-9]", "", regex=True)
        )
        clean_data["Exp"] = pd.to_numeric(
            clean_data["Exp"], errors="coerce"
        )

        # Report rows that failed to parse (became NaN)
        bad_rows = clean_data[
            clean_data["Salary"].isna() | clean_data["Exp"].isna()
        ]

        if not bad_rows.empty:
            st.warning(
                f"{len(bad_rows)} row(s) had unparseable Salary/Exp values "
                "and were set to NaN. Review below."
            )
            st.dataframe(bad_rows)

        fill_option = st.radio(
            "How should missing/invalid values be handled?",
            ["Fill with 0", "Drop rows", "Leave as NaN (nullable Int64)"],
        )

        if fill_option == "Fill with 0":
            clean_data["Salary"] = clean_data["Salary"].fillna(0).astype(int)
            clean_data["Exp"] = clean_data["Exp"].fillna(0).astype(int)
        elif fill_option == "Drop rows":
            clean_data = clean_data.dropna(subset=["Salary", "Exp"])
            clean_data["Salary"] = clean_data["Salary"].astype(int)
            clean_data["Exp"] = clean_data["Exp"].astype(int)
        else:
            clean_data["Salary"] = clean_data["Salary"].astype("Int64")
            clean_data["Exp"] = clean_data["Exp"].astype("Int64")

        st.subheader("Cleaned Data Preview")
        st.dataframe(clean_data.head(20))

        st.subheader("Summary Stats")
        st.write(clean_data[["Salary", "Exp"]].describe())

        csv_out = clean_data.to_csv(index=False).encode("utf-8")
        st.download_button(
            "Download Cleaned CSV",
            data=csv_out,
            file_name="cleaned_data.csv",
            mime="text/csv",
        )
else:
    st.info("Upload a CSV file to get started.")
