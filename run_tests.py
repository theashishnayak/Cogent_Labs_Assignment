import subprocess
import os

def run_behave_tests():
    report_dir = "reports"
    if not os.path.exists(report_dir):
        os.makedirs(report_dir)

    # Note: Ensure behave.ini is properly configured for HTML formatter
    command = "behave -f html -o {}/report.html".format(report_dir)
    subprocess.run(command, shell=True, check=True)

if __name__ == "__main__":
    run_behave_tests()