import generate_testcharta
import run_test_session
import asyncio
from analyze_page_with_browser_use import main

asyncio.run(main())
input("go on? Press Enter to continue...")  # wait for user input before proceeding
generate_testcharta.run()
input("go on? Press Enter to continue...")  # wait for user input before proceeding
run_test_session.run("https://automationintesting.online/")
