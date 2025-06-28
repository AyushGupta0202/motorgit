# PyPI Upload Guide for Motorgit (macOS)

This guide documents the exact steps to successfully upload the `motorgit` package to PyPI, including how to resolve common SSL and metadata issues on macOS (especially with Homebrew Python).

---

## 1. **Version Bump**
- Update the version in `Constants.py` (e.g., `version = '1.0.2'`).

## 2. **No Need to Delete License File!**
- The license file has been renamed to `LICENSE_MOTORGIT.txt` to avoid PyPI metadata issues. No need to delete or restore it for uploads.

## 3. **Clean Build Artifacts**
- Remove old build directories:
  ```sh
  rm -rf build dist motorgit.egg-info
  ```

## 4. **Build the Distributions**
- Rebuild the source and wheel distributions:
  ```sh
  python3 setup.py sdist bdist_wheel
  ```

## 5. **Upload to PyPI (Use System Python!)**
- Homebrew Python often fails SSL verification. Use the system Python, which has the correct certificates:
  ```sh
  /usr/bin/python3 -m pip install --user --upgrade twine
  /usr/bin/python3 -m twine upload dist/*
  ```
- If you see SSL errors, do **not** use Homebrew Python for the upload.

## 6. **Verify on PyPI**
- Check your package at: https://pypi.org/project/motorgit/

---

## **Troubleshooting**

### **SSL Certificate Errors**
- If you see errors like:
  ```
  SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] ...')
  ```
- Always use `/usr/bin/python3` for the upload step on macOS.
- If you installed Python from python.org, run:
  ```sh
  /Applications/Python\ 3.x/Install\ Certificates.command
  ```

### **License-File Metadata Error**
- This is now avoided by renaming the license file to `LICENSE_MOTORGIT.txt`.

---

## **Summary**
- Always use the system Python for PyPI uploads on macOS.
- The license file is now named `LICENSE_MOTORGIT.txt` to avoid metadata errors.
- No need to delete or restore the license file for uploads.

**This process is proven to work and avoids all known issues with PyPI uploads for this project.** 