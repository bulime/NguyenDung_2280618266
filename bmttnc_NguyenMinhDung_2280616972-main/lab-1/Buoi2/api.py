from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher

app = Flask(__name__)
caesar_cipher = CaesarCipher()

@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    data = request.json
    plain_text = data["text"]
    key = int(data["key"])
    encrypted_text = caesar_cipher.encrypt(plain_text, key)
    return jsonify({"encrypted_message": encrypted_text})

@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    data = request.json
    cipher_text = data.get("text")
    key = int(data.get("key"))
    decrypted_text = caesar_cipher.decrypt(cipher_text, key)
    return jsonify({"decrypted_message": decrypted_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

