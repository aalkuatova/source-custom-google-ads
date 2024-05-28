from setuptools import find_packages, setup

MAIN_REQUIREMENTS = [
    "airbyte-cdk==0.80.0", 
    "google-ads==24.0.0", 
    "protobuf==4.25.2", 
    "pendulum<3.0.0"
    ]

TEST_REQUIREMENTS = [
    "pytest~=6.1", 
    "pytest-mock~=3.12.0", 
    "freezegun~=1.4.0", 
    "requests-mock~=1.11.0"
    ]

setup(
    entry_points={
        "console_scripts": [
            "source-google-ads=source_google_ads.run:run",
        ],
    },

    name="source_google_ads",
    description="Source implementation for Google Ads.",
    author="Airbyte",
    author_email="contact@airbyte.io",
    packages=find_packages(),
    install_requires=MAIN_REQUIREMENTS,
    package_data={"": ["*.json", "schemas/*.json", "schemas/shared/*.json"]},
    extras_require={
        "tests": TEST_REQUIREMENTS,
    },
)