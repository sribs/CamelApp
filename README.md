# RESTful Services string to CamelCase Converter using Python Flask

String to CamelCase coverter using Zipf's Law.

## Motivation
picking a word from the English Dictionary is uniformly distributed. So, using relative frequencies for all the words is reasonable and Zipf's law makes use of the same underlying theory.

#### Taken from Wikipedia:
Zipf's law states that given a large sample of words used, the frequency of any word is inversely proportional to its rank in the frequency table. So word number n has a frequency proportional to 1/n.

Thus the most frequent word will occur about twice as often as the second most frequent word, three times as often as the third most frequent word, etc. For example, in one sample of words in the English language, the most frequently occurring word, "the", accounts for nearly 7% of all the words (69,971 out of slightly over 1 million). True to Zipf's Law, the second-place word "of" accounts for slightly over 3.5% of words (36,411 occurrences), followed by "and" (28,852). Only about 135 words are needed to account for half the sample of words in a large sample.


## Assumptions
1. The input shall be string of non-spaced lowercase english alphabet or integers
2. No dictionary API is needed.
3. Pre-requisites are installed and if using Azure, knowledge of Creating containerized applications using Azure AppServices or creating container instance

## Reasons for Change
1. Limited number of requests in Oxford Dictionary
2. Unable to scale for very large strings due to (1).
3. Not using Trie because of a better algorithm

## Design
1. `CamelCase.py`: Class which contains the implementation of string to CamelCase coversion
2. `JSONOps.py` : Class for Handling JSON Operations for RESTful Services
3. `CamelFlask.py` : Python Flask RESTful webservice running on port 80
4. `files/CamelCase.json` : JSON file used for File Storage during RESTful Services Operations

## Usage
#### API Setup
##### Using in Physical Machines
   ``` bash
   root@localhost $ git clone https://github.com/sribs/CamelApp.py  
   root@localhost $ python CamelApp/CamelFlask.py
   ```
##### Using Containers Commandline
   ``` bash
   root@localhost $ docker run sriharshabs/camelcaseapp:latest
   ```
##### Using Azure Container Instance or Azure AppService
    Please follow the Portal On Screen Instructions
#### API Usage
1. To get all CamelCase strings, `https://camelcase.azurewebsites.net/all`
2. To perform a GET, POST, PUT or DELETE for a particular string, `https://camelcase.azurewebsites.net/camelcase/<strname>`

## Output
    (base) C:\Users\Sriharsha B S\Desktop\CamelCase\CamelApp>curl -v -X GET https://camelcase.azurewebsites.net/all         Note: Unnecessary use of -X or --request, GET is already inferred.                                                      *   Trying 52.165.184.170...                                                                                            * TCP_NODELAY set                                                                                                       * Connected to camelcase.azurewebsites.net (52.165.184.170) port 443 (#0)                                               * schannel: SSL/TLS connection with camelcase.azurewebsites.net port 443 (step 1/3)                                     * schannel: checking server certificate revocation                                                                      * schannel: sending initial handshake data: sending 192 bytes...                                                        * schannel: sent initial handshake data: sent 192 bytes                                                                 * schannel: SSL/TLS connection with camelcase.azurewebsites.net port 443 (step 2/3)                                     * schannel: failed to receive handshake, need more data                                                                 * schannel: SSL/TLS connection with camelcase.azurewebsites.net port 443 (step 2/3)                                     * schannel: encrypted data got 4096                                                                                     * schannel: encrypted data buffer: offset 4096 length 4096                                                              * schannel: received incomplete message, need more data                                                                 * schannel: SSL/TLS connection with camelcase.azurewebsites.net port 443 (step 2/3)                                     * schannel: encrypted data got 1024                                                                                     * schannel: encrypted data buffer: offset 5120 length 5120                                                              * schannel: received incomplete message, need more data                                                                 * schannel: SSL/TLS connection with camelcase.azurewebsites.net port 443 (step 2/3)                                     * schannel: encrypted data got 445                                                                                      * schannel: encrypted data buffer: offset 5565 length 6144                                                              * schannel: sending next handshake data: sending 126 bytes...                                                           * schannel: SSL/TLS connection with camelcase.azurewebsites.net port 443 (step 2/3)                                     * schannel: encrypted data got 51                                                                                       * schannel: encrypted data buffer: offset 51 length 6144                                                                * schannel: SSL/TLS handshake complete                                                                                  * schannel: SSL/TLS connection with camelcase.azurewebsites.net port 443 (step 3/3)                                     * schannel: stored credential handle in session cache                                                                   > GET /all HTTP/1.1                                                                                                     > Host: camelcase.azurewebsites.net                                                                                     > User-Agent: curl/7.55.1                                                                                               > Accept: */*                                                                                                           >                                                                                                                       * schannel: client wants to read 102400 bytes                                                                           * schannel: encdata_buffer resized 103424                                                                               * schannel: encrypted data buffer: offset 0 length 103424                                                               * schannel: encrypted data got 342                                                                                      * schannel: encrypted data buffer: offset 342 length 103424                                                             * schannel: decrypted data length: 313                                                                                  * schannel: decrypted data added: 313                                                                                   * schannel: decrypted data cached: offset 313 length 102400                                                             * schannel: encrypted data buffer: offset 0 length 103424                                                               * schannel: decrypted data buffer: offset 313 length 102400                                                             * schannel: schannel_recv cleanup                                                                                       * schannel: decrypted data returned 313                                                                                 * schannel: decrypted data buffer: offset 0 length 102400                                                               < HTTP/1.1 200 OK                                                                                                       < Content-Length: 26                                                                                                    < Content-Type: application/json                                                                                        < Server: Werkzeug/0.14.1 Python/3.7.2                                                                                  < Set-Cookie: ARRAffinity=87619c1bcf9edccdaac372052beb202b1e23bea2f0bb9af0a9b2e6d69dff1808;Path=/;HttpOnly;Domain=camelcase.azurewebsites.net                                                                                                   < Date: Sun, 03 Mar 2019 06:34:56 GMT                                                                                   <                                                                                                                       {"one":"One","two":"Two"}                                                                                               * Connection #0 to host camelcase.azurewebsites.net left intact  