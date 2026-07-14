# AI Fix Summary

**Error:** Unknown error

**Suggested Fix:** **Step 1: Identify the File or Directory Not Found**

* Review the error message: `COPY failed: file not found`
* Check the path specified in the `COPY` instruction.
* Ensure the file or directory actually exists in the build context.

**Step 2: Check the Build Context**

* Verify that the context directory contains the file or directory being copied.
* Use the `pwd` command to check the current working directory.
* Check if the file or directory exists in the context using `ls -l`.

**Step 3: Resolve ModuleNotFoundError**

* Identify the missing package in the error message.
* Check if the package is installed in the Docker environment.
* If not, add it to the `requirements.txt` file.
* If already installed, ensure it's compatible with the current Python version.

**Step 4: Verify Dependencies and Build Order**

* Review the `requirements.txt` file and ensure the file is listed correctly.
* Check the build order and ensure the file is referenced after the package is installed.

**Step 5: Provide a Clear Fix Plan**

* Clearly describe the issue and steps to reproduce it.
* Provide the expected behavior and the actual result.
* Include any relevant context, such as the project setup and dependencies.

**Example Fix Plan:**

```
**Issue:** COPY failed: file not found

**Step 1:** Check the path in the `COPY` instruction and ensure the file exists.
**Step 2:** Verify the file or directory is present in the build context.
**Step 3:** Add the missing package to `requirements.txt` or install it in the Dockerfile.
**Step 4:** Review the `requirements.txt` file and ensure the file is listed correctly.
**Step 5:** Verify the build order and ensure the file is referenced after the package is installed.
```