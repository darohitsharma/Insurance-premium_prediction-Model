"""Educational Streamlit interface. Requires a separately verified trusted model."""
import math
import os
from pathlib import Path
import streamlit as st
from features import encode_features


def main():
    st.set_page_config(page_title='Insurance expense model demo', page_icon='📊', layout='centered')
    st.title('Insurance expense model demo')
    st.warning('Learning project only. Not an insurer quote, coverage recommendation, medical advice or a validated pricing tool.')
    st.caption('No input is saved by this code. Model output is a dataset expense estimate, not a promised premium.')
    model_path = Path(os.environ.get('INSURANCE_MODEL_PATH', 'artifacts/model.joblib'))
    if not model_path.is_file():
        st.info('No verified model artifact is installed. Review SETUP.md and MODEL_CARD.md. The app will not load the legacy mislabeled binary automatically.')
        st.code('INSURANCE_MODEL_PATH=/private/path/to/verified-model.joblib')
        st.stop()
    if os.environ.get('INSURANCE_TRUST_MODEL') != 'true':
        st.error('Model loading is off. Pickle/joblib can execute code. Verify the artifact and its environment first, then set INSURANCE_TRUST_MODEL=true locally.')
        st.stop()
    with st.form('features'):
        age = st.number_input('Age', min_value=18, max_value=100, value=25)
        sex = st.selectbox('Sex category used by this historical dataset', ('female', 'male'))
        bmi = st.number_input('BMI', min_value=0.1, max_value=100.0, value=25.0)
        children = st.selectbox('Number of children', (0, 1, 2, 3, 4, 5))
        smoker = st.selectbox('Smoker category', ('no', 'yes'))
        region = st.selectbox('Dataset region', ('southwest', 'southeast', 'northwest', 'northeast'))
        submit = st.form_submit_button('Estimate dataset expense')
    if not submit:
        return
    try:
        vector = encode_features(age, sex, bmi, children, smoker, region)
        import joblib
        model = joblib.load(model_path)
        if hasattr(model, 'n_features_in_') and model.n_features_in_ != 6:
            raise ValueError('Model feature count does not match the documented contract.')
        prediction = float(model.predict([vector])[0])
        if not math.isfinite(prediction) or prediction < 0:
            raise ValueError('Invalid model output.')
    except Exception:
        st.error('The trusted artifact could not produce a valid estimate with the documented six-feature contract. Check its training environment privately.')
        return
    st.metric('Unvalidated expense estimate, dataset units', f'{prediction:,.2f}')
    st.caption('Currency, coverage period and present-day applicability have not been verified. Do not use this estimate for purchasing or pricing insurance.')


if __name__ == '__main__':
    main()
