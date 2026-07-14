# AI Fix Summary

**Error:** Unknown error

**Suggested Fix:** **Step 1: Identify the File or Directory Not Found**

* Review the error message: `COPY failed: file not found`
* This indicates that the file or directory being copied does not exist in the build context.
* Check the path specified in the `COPY` instruction.

**Step 2: Verify File or Directory Existence**

* Ensure that the file or directory actually exists in the build context.
* Use the `-p` flag with `docker build` to specify the source and destination paths explicitly.
* Check the build logs for any errors or warnings related to the missing file.

**Step 3: Resolve ModuleNotFoundError**

* If the file or directory is present but the required package is missing, use the following solutions:
    * Add the missing package to the `requirements.txt` file.
    * Install the package in the Dockerfile using `RUN pip install <package_name>`.

**Step 4: Provide a Clear Fix Plan**

* Clearly describe the issue and provide a step-by-step fix plan.
* Include the following information:
    * The specific command used in the `COPY` instruction.
    * Any error messages or warnings encountered.
    * Any changes made to the build context or Dockerfile.

**Example Fix Plan:**

```
**Issue:** COPY failed: file not found

**Step 1:** Verify file existence

* Use `docker build -v <source_path>:<destination_path>` to specify the source and destination paths.
* Check the build logs for any errors or warnings.

**Step 2:** Resolve ModuleNotFoundError

* Add the missing package to `requirements.txt` or install it in the Dockerfile.
* Update the `COPY` instruction to use the package name.

**Additional Tips:**

* Use a linter like `docker-compose lint` to identify potential errors in the Dockerfile.
* Use a build tool like `docker-compose build` to automate the build process and handle dependencies.
* Share the complete build command and any relevant logs for further troubleshooting.