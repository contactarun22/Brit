# Brit Insurance Demo
Brit Insurance Demo

This test suite utilizes pytest for automated testing of Brit Insurance Home page.

## Author

- [Arun S](https://github.com/contactarun22)

## DEMO Video Recording

[Click here to watch the video](https://vimeo.com/902466529?share=copy)


## Running Tests

### Prerequisites

- Python installed
- Pip package manager installed

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your_username/project-name.git
    cd project-name
    ```

2. **Create a Virtual Environment:**

   Open a terminal or command prompt, navigate to your project directory, and run the following command to create a virtual environment named `venv`:

   ```bash
   python -m venv venv

3. Activate the Virtual Environment

   ```bash
   venv\Scripts\activate #Windows
   source venv/bin/activate   #Mac

4. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Running Tests

To run the tests, use the following commands

```bash
pytest
```

### Headless Mode

By default, the tests run in non-headless mode. To run the tests in headless mode, use the --headless option:
```bash
pytest --headles
```

### Running Tests with Different Log Levels

To run the tests with different log levels, use the following command:

```bash
pytest --log-cli-level=LEVEL
```
Replace LEVEL with any one of the below:

critical: Only critical errors are displayed.

error: Errors and critical errors are displayed.

warning: Warnings, errors, and critical errors are displayed.

info: Info messages, warnings, errors, and critical errors are displayed.

debug: Debug messages, info messages, warnings, errors, and critical errors are displayed.

### Using Markers

This test suite utilizes markers to categorize tests. To run tests based on markers, use the `-m` option with pytest.

For example, to run only smoke tests:

```bash
`pytest -m smoke`
```

This is based on the markers that are added to each of the tests. Smoke,regression,API,UI

### Log File Format

The log file generated during test execution follows the format:

```bash
`test_log_YEAR-MONTH-DAY_HOUR-MINUTE-SECOND.log`
```

The log file contains entries in the following format:

```bash
`[TIME] - [LOG LEVEL] - [MESSAGE]`
```

Here is an example entry:

```bash
`2024-01-10 15:30:45 - INFO - Test session started.`
```

### HTML REPORTS For Run

HTML reports can also be generated for the runs.
By triggering the run with below command

```bash
 pytest --html=reports/report.html
```

That will look something like this

![Alt Text](ReportScreenshot.png)


### Build Docker Image and Run Docker

1. Build the Docker image:

```
docker build -t brit-app .
```

2. Run the docker container:

```
docker run brit-app
```

![Alt Text](DockerScreeenshot.png)



