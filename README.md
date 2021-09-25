# mydro.ga
Project for the HackZurich 2021 event

# Usage

PUT:
 `curl -H 'Content-Type: multipart/form-data' -v -X PUT -F qr_code=qr_val -F 'file=@/home/riccardo/Github/mydro/mypdf.txt' http://127.0.0.1:5000/put/paracetamol2`

GET:
`curl http://127.0.0.1:5000/get/barcode/speed`