from streamlit.testing.v1 import AppTest

def test_app_boots_without_crashing():
    """Simulate starting the Streamlit app to ensure no fatal errors on load."""
    
    # 1. Point the testing robot to your main app file
    at = AppTest.from_file("app.py")
    
    # 2. Tell the robot to 'run' the app (like a user opening the page)
    at.run()
    
    # 3. Assert that no background Python errors or exceptions occurred
    assert not at.exception
    
def test_ui_components_load():
    """Simulate a user checking the screen to verify the main controls exist."""
    
    # 1. Initialize the ghost browser again
    at = AppTest.from_file("app.py")
    at.run()
    
    # 2. Assert that at least one File Uploader box exists on the page
    assert len(at.file_uploader) > 0
    
    # 3. Assert that the drop-down menu (Selectbox) exists on boot
    assert len(at.selectbox) > 0