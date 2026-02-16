import sys

def test_facepy_resurrection():
    try:
        # THE TRIPWIRE: 
        # Inside Facepy, it tries to access requests.packages.urllib3.
        # Modern 'requests' has removed this, causing a hard crash.
        from facepy import GraphAPI
        
        # Simple initialization check
        graph = GraphAPI('dummy_token')
        
        print("✅ Validation Passed: Facepy engine successfully initialized.")
        return True
        
    except AttributeError as e:
        print(f"❌ Validation Failed: Internal Library Crash (Requests API Removal). {e}")
        sys.exit(1)
    except ImportError as e:
        print(f"❌ Validation Failed: Import error. {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Validation Failed: Runtime crash. {e}")
        sys.exit(1)

if __name__ == "__main__":
    test_facepy_resurrection()