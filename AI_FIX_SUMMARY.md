# AI Fix Summary

**Error:** Unknown error

**Suggested Fix:** **Step 1: Identify the File or Directory Not Found**

* Review the error message: `COPY failed: file not found`
* This indicates that the file or directory being copied does not exist in the build context.

**Step 2: Check the Path in the COPY Instruction**

* Ensure that the path in the `COPY` instruction is correct and points to the actual file or directory.
* Use absolute paths if possible to ensure the file is located in the build context.

**Step 3: Verify the File or Directory Existence**

* Check if the file or directory actually exists in the build context.
* Use the `-f` flag with the `ls` command to verify the file's existence.
* If the file is missing, add it to the build context using the `docker context add` command.

**Step 4: Resolve ModuleNotFoundError**

* If the file or directory is present but the required package is missing, use the `pip install` command to install it.
* Add the package to the `requirements.txt` file and rebuild the image.

**Step 5: Provide a Clear Fix Plan**

* Clearly describe the issue and provide a step-by-step fix plan.
* Include the following information:
    * The specific error message
    * The file or directory not found
    * Any steps taken to resolve the issue
    * The expected outcome

**Example Fix Plan:**

```
**Step 1:** Identify the file not found

```

**Step 2:** Check the path in the `COPY` instruction

```
COPY ./src /app/src
```

**Step 3:** Verify the file or directory existence

```
-f ls ./src
```

**Step 4:** Resolve ModuleNotFoundError

```
pip install requests==2.31.0
```

**Step 5:** Provide a clear fix plan

```
**Issue:** Unknown error

**Root Cause:** Docker build context does not contain the file or directory.

**Solution:** Add the file or directory to the build context using the `docker context add` command.