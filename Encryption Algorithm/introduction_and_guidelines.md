Creating a secure encryption algorithm is a complex and specialized task that requires a deep understanding of cryptography and security principles. While your approach of using invertible matrices and matrix multiplication can be a foundation for an encryption scheme, there are several important considerations to keep in mind to ensure the security of your algorithm. Here are some suggestions to make your encryption process more complex and stronger:

1. **Key Generation**: The security of your encryption scheme heavily relies on the secrecy of the key. Generating strong and unpredictable keys is essential. Consider using a cryptographically secure random number generator to create your keys.

2. **Matrix Size and Padding**: You mentioned using padding to fit data into a square matrix. The choice of padding can affect security. Make sure your padding scheme is not predictable or exploitable.

3. **Multiple Rounds**: Instead of a single matrix multiplication, consider using multiple rounds of matrix multiplication with different keys. Each round should utilize a different key and matrix. This technique is often used in block ciphers like AES.

4. **Key Mixing**: Combine the keys in a non-trivial way before using them for matrix multiplication. This can make it harder for attackers to reverse engineer the encryption process.

5. **Non-Linear Operations**: Incorporate non-linear operations within the encryption process. This can be achieved through techniques like applying a nonlinear function to the matrix elements after each multiplication round.

6. **S-Boxes or Substitution Layers**: Introduce substitution layers like S-Boxes used in modern encryption algorithms. These layers can add complexity and confusion to the encryption process.

7. **Avalanche Effect**: Ensure that small changes in the input data or key result in significant changes in the encrypted output. This property is known as the avalanche effect and is crucial for security.

8. **Key Management**: Implement a robust key management system. Keys should be securely stored, rotated, and managed to prevent unauthorized access.

9. **Cryptanalysis**: Regularly assess your algorithm's security by subjecting it to cryptanalysis. Invite security experts to analyze your algorithm for vulnerabilities.

10. **Peer Review**: Open your algorithm to peer review from the cryptography community. This can help identify potential weaknesses and improve the overall security.

11. **Standardization**: If your goal is to create a strong encryption algorithm, consider submitting it to cryptographic standardization processes like NIST's Cryptographic Algorithm Validation Program (CAVP). This can provide external validation of your algorithm's security.

12. **Attacks and Countermeasures**: Study known cryptographic attacks and countermeasures to understand potential weaknesses in your approach. This can help you design your algorithm with these threats in mind.

Remember that designing a secure encryption algorithm is an intricate and challenging task. Cryptanalysis is an essential step to ensure that your algorithm can withstand various attacks. Additionally, using well-established and peer-reviewed encryption algorithms, like AES, is often recommended for practical applications due to their proven security properties.