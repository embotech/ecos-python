xcopy /e "%RECIPE_DIR%\..\.." "%SRC_DIR%"
"%PYTHON%" -m pip install wheel
"%PYTHON%" setup.py install bdist_wheel
if errorlevel 1 exit 1
