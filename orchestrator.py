#!/usr/bin/env python3
import argparse
import time
import json
from agent import CICDAssistant
from monitoring import MetricsCollector
from config import Config

def main():
    parser = argparse.ArgumentParser(description="AI Pipeline Assistant")
    parser.add_argument("--source", choices=["sample", "file", "github"], default="sample",
                        help="Log source")
    parser.add_argument("--file", help="Path to log file if source=file")
    parser.add_argument("--no-fix", action="store_true", help="Disable auto-fix")
    args = parser.parse_args()
    
    assistant = CICDAssistant(auto_fix=not args.no_fix)
    metrics = MetricsCollector()
    
    if args.source == "sample":
        log_content = """
        ====== BUILD STARTED ======
        Step 1: Checking out code... ✓
        Step 2: Installing dependencies...
        ERROR: ModuleNotFoundError: No module named 'requests'
        Build failed.
        """
    elif args.source == "file" and args.file:
        with open(args.file, 'r') as f:
            log_content = f.read()
    else:
        log_content = """
        ====== BUILD STARTED ======
        ERROR: Could not find a version that satisfies the requirement requests==2.28.0
        """
    
    start = time.time()
    result = assistant.process_failure(log_content)
    duration = time.time() - start
    
    success = result.get("pr") is not None
    error_type = result["analysis"].get("error", "unknown")
    metrics.record(success, error_type, duration)
    
    print(json.dumps(result, indent=2, default=str))
    print(f"\n✅ Done in {duration:.2f}s")
    if success:
        print(f"PR: {result['pr']['pr_url']}")
    else:
        print("No PR created (maybe auto-fix was disabled or failed).")

if __name__ == "__main__":
    main()