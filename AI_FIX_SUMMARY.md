# AI Fix Summary

**Error:** Unknown error

**Suggested Fix:** **Step 1: Identify the File or Directory Not Found**

* Review the error message: "COPY failed: file not found".
* This indicates that the file or directory being copied does not exist in the build context.
* Check the path specified in the `COPY` instruction.

**Step 2: Check the Build Context**

* Ensure that the file or directory you are trying to copy actually exists in the build context.
* Use the `pwd` command to verify the current working directory.
* If the file is missing, add it to the build context using the `docker context add` command.

**Step 3: Verify the File Path**

* Ensure that the file path in the `COPY` instruction is correct and accurate.
* Use double quotes for paths with spaces or special characters.
* Check if the file is case-sensitive.

**Step 4: Solve ModuleNotFoundError**

* Check if the required package is installed in the Docker environment.
* If not, add it to the `requirements.txt` file or build the package within the Dockerfile.
* Ensure that the package is compatible with the Python version being used.

**Step 5: Provide a Clear Fix Plan**

* Clearly describe the issue and the steps taken to resolve it.
* Provide specific details about the file or directory not found, the required package, and any other relevant information.
* Include a summary of the solution and the expected outcome.

**Example Fix Plan:**

```
**Issue:** Docker build fails with "COPY failed: file not found"

**Steps:**

1. Check the build context and ensure the file is present.
2. Verify the file path in the `COPY` instruction.
3. Install the required package if it is missing.
4. Add the missing package to the `requirements.txt` file.
5. Build the Docker image with the updated context and requirements.
```