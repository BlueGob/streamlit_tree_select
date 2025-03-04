import setuptools

setuptools.setup(
    name="streamlit-tree-selector",
    version="1.0.0",
    author="BlueGob",
    author_email="",
    description="A simple and elegant checkbox tree for Streamlit.",
    long_description="",
    long_description_content_type="text/plain",
    url="https://github.com/BlueGob/streamlit_tree_select",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.6",
    install_requires=[
        # By definition, a Custom Component depends on Streamlit.
        # If your component has other Python dependencies, list
        # them here.
        "streamlit >= 0.63",
    ],
)
