"""Feature order/encoding from the existing training notebook, not a clinical rule."""
import math

FEATURES = ('age', 'sex', 'bmi', 'children', 'smoker', 'region')
SEX = {'female': 0, 'male': 1}
SMOKER = {'no': 0, 'yes': 1}
REGION = {'southwest': 1, 'southeast': 2, 'northwest': 3, 'northeast': 4}


def encode_features(age, sex, bmi, children, smoker, region):
    age_value = float(age)
    child_value = float(children)
    bmi_value = float(bmi)
    if not all(math.isfinite(v) for v in (age_value, child_value, bmi_value)):
        raise ValueError('Numeric inputs must be finite.')
    if not age_value.is_integer() or not 18 <= age_value <= 100:
        raise ValueError('Demo age must be an integer from 18 to 100.')
    if not child_value.is_integer() or not 0 <= child_value <= 5:
        raise ValueError('Demo children count must be an integer from 0 to 5.')
    if not 0 < bmi_value <= 100:
        raise ValueError('Demo BMI must be greater than 0 and at most 100.')
    try:
        return [int(age_value), SEX[str(sex).lower()], bmi_value,
                int(child_value), SMOKER[str(smoker).lower()], REGION[str(region).lower()]]
    except KeyError:
        raise ValueError('Unknown categorical value.') from None
