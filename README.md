## Setup environment

conda create --name streamlit python=3.9
conda activate streamlit
pip install numpy pandas scipy matplotlib seaborn streamlit

cd dashboard

## Run steamlit app

streamlit run Dashboard.py
