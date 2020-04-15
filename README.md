# ICS -> Combination of PlayFair, Rail Transformation, OneTimePad

### Drawback of Playfair

	As the key and matrix of playfair remains constant for the entire encryption 
	pairs containing same letters get encrypted to same cipher. This is a potential 
	vulnerability.

	To overcome this, I built this new script which combines the disposition of rail 
	fence and power of One Time Pad, with playfair to encrypt in most secure fashion

### Why rail fence?
	
	* Because easy to implement
	* Faster execution when length of keyword is huge compared to row/columnar transposition.

### Why One Time Pad?

	* If the length of keyword is short, then after a few rail fence transformations we get the original keyword sequence.
	* To avoid this we randomly generate a keyword for every communication, having length equal to the length of message.

### How this works?

#### Encryption

	1. User enters a message.
	2. It is then preprocessed.
		* White spaces and punctuation is removed.
	3. Keyword is generated using random chars(excluding *j*) of len(message)
	4. Pairs of message are generated.
	5. Rail fence transformation is applied on keyword for n times (where n=number of pairs) and stored into array of keys.
	6. For each pair
		* Generate matrix with key[i] (i is number of the current pair)
		* Use that matrix to encrypt pair in playfair fashion.
		* Add the encrypted pair to ciphertext string.

#### Decryption

	* Decryption follows the same high level flow, except instead of using encryption function of playfair, 
	  we use decryption function.
