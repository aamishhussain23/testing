from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import secrets
import string

app = FastAPI()

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Function to generate a unique 16-character code
def generate_unique_code(existing_codes):
    alphabet = string.ascii_letters + string.digits
    while True:
        code = ''.join(secrets.choice(alphabet) for _ in range(16))
        if code not in existing_codes:
            existing_codes.add(code)
            break
    return code

# Set to store existing codes
existing_codes = set()

@app.get("/")
def read_root():
    # Generate a new unique code
    new_code = generate_unique_code(existing_codes)
    return {"Unique 16-character code": new_code}
