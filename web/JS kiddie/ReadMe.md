# JavaScript
## Problem
The problem is in the link below
https://2019shell1.picoctf.com/problem/59857/
There's only an input field.
![](https://i.imgur.com/qxM7n2d.png)
If we look in the source we can see the script in html file.
```JavaScript=

var bytes = [];
$.get("bytes", function(resp) {
bytes = Array.from(resp.split(" "), x => Number(x));});

function assemble_png(u_in){
    var LEN = 16;
	var key = "0000000000000000";
	var shifter;
	if(u_in.length == LEN){
		key = u_in;
		}
	var result = [];
	for(var i = 0; i < LEN; i++){
	shifter = key.charCodeAt(i) - 48;
	for(var j = 0; j < (bytes.length / LEN); j ++){
	result[(j * LEN) + i] = bytes[(((j + shifter) * LEN) % bytes.length) + i]
			}
		}
	while(result[result.length-1] == 0){
		result = result.slice(0,result.length-1);
				}
	document.getElementById("Area").src = "data:image/png;base64," + btoa(String.fromCharCode.apply(null, new Uint8Array(result)));
	return false;
}

```

In line3, after we click submit, it will send request to bytes. Adding 'bytes' at teh and of the link, we get a long string
```
204 182 91 198 74 66 60 251 217 163 0 0 0 255 183 91 82 181 39 63 173 10 255 102 0 251 0 13 0 222 131 127 247 155 127 47 75 0 91 247 0 182 156 0 73 0 64 227 73 227 78 117 229 73 67 118 1 120 232 237 0 0 205 0 137 69 78 185 129 12 84 130 84 43 178 163 154 72 255 0 0 80 1 177 174 1 217 10 33 0 45 144 200 192 120 82 164 0 0 175 13 84 237 114 96 0 55 30 100 77 120 108 48 0 133 2 0 159 96 65 182 0 128 222 20 55 0 220 51 16 40 68 143 144 26 148 227 120 32 145 120 187 0 114 12 233 60 71 139 153 1 217 140 7 140 104 228 85 68 153 81 67 140 114 128 210 68 154 164 243 197 223 2 227 95 31 254 248 158 2 59 0 189 1 213 252 58 244 153 48 138 55 195 61 122 223 111 52 121 0 1 141 251 241 161 224 27 119 128 129 0 115 58 128 45 146 9 29 252 244 104 31 59 112 234 19 59 78 223 189 194 255 95 12 3 84 250 122 174 132 135 7 30 165 73 205 236 27 85 122 138 195 222 61 141 223 45 239 8 213 61 54 15 24 68 160 128 127 107 141 182 127 239 175 69 140 25 245 61 230 255 36 55 30 55 73 39 61 214 37 252 39 202 147 248 210 123 220 29 150 227 55 107 142 139 99 135 144 72 248 19 169 113 2 250 225 78 67 140 159 189 136 240 158 124 136 34 198 6 170 4 141 223 191 198 116 48 17 72 64 126 50 19 186 253 217 48 77 255 56 255 231 245 146 231 0 42 31 207 56 157 119 6 59 80 32 154 179 39 191 56 62 75 74 253 58 198 240 69 113 41 192 181 223 34 132 64 32 151 90 14 153 23 205 135 0 243 244 202 240 20 100 77 55 0 64 4 96 191 108 73 92 102 194 130 225 212 159 217 36 204 209 157 234 239 106 220 245 125 116 245 51 102 250 61 228 241 147 77 250 38 86 216 54 27 214 140 107 217 254 92 131 123 30 38 18 74 190 48 65 83 89 202 70 177 52 22 177 95 252 216 198 146 227 241 188 177 255 83 87 188 172 74 191 225 38 190 214 200 204 63 251 118 91 181 213 47 219 242 252 38 47 223 118 70 248 253 159 242 53 61 62 142 79 99 53 250 110 61 175 198 0 178 250 140 16 249 28 240 214 16 196 164 85 28 254 0 226 180 46 117 75 230 66 228 19 184 80 14 248 81 58 175 103 33 45 44 175 158 180 101 98 22 171 92 75 32 240 79 143 190 207 162 54 126 95 143 87 245 34 73 90 221 141 230 44 121 100 172 230 193 158 155 111 207 252 82 196 88 169 102 20 164 89 96 205 70 136 230 127 251 242 175 15 77 86 71 226 253 190 45 225 127 231 250 215 255 90 183 24 94 80 242 189 199 88 205 189 223 156 225 141 61 70 27 125 85 182 252 27 253 248 164 100 255 193 211 72 44 149 15 126 109 246 31 106 255 243 125 159 107 148 101 205 245 198 239 127 61 95 103 8 227 61 242 171 191 166 12 146 191 147 255 200 3 119 30 76 14 141 43 249 252 248 163 192 190 128 244 24 111 247 215 227 0 178 55 109 196 124
```
From the code, we can see the long string is used to encoded by the input we type in and become a new string.

```javascript=
 var LEN = 16;
	var key = "0000000000000000";
	var shifter;
	if(u_in.length == LEN){key = u_in;}
```
From here, we can see the length of value we key in should be 16.
```javascript=
var result = [];
for(var i = 0; i < LEN; i++){
	shifter = key.charCodeAt(i) - 48;
	for(var j = 0; j < (bytes.length / LEN); j ++){
	result[(j * LEN) + i] = bytes[(((j + shifter) * LEN) % bytes.length) + i]
			}
		}
	while(result[result.length-1] == 0){
		result = result.slice(0,result.length-1);
				}
	document.getElementById("Area").src = "data:image/png;base64," + btoa(String.fromCharCode.apply(null, new Uint8Array(result)));
	return false;
```
Above is how the website use the input as a string to encode the bytes string.
From the problem description: 
`The image link appears broken...`
we can guess that the result after encoding by the key should be an image.

```javascript=
document.getElementById("Area").src = "data:image/png;base64," + btoa(String.fromCharCode.apply(null, new Uint8Array(result)));
```
From above, I guess the image should be an PNG file. Furthemore, the header of png should be
`137, 80, 78, 71, 13, 10, 26, 10,0,0,0,13,73,72,68,82`

The clues above should provide us a way to solve the problem: Find the original string by encoding reversely with the correct key.

Now, write a program to find the key which can help generagte the image. The bytes are the result after the png being encoded with the key we type in. We need to garuantee that the reversely encoded string has the correct header.
```javascript=
var string="204 182 91 198 74 66 60 251 217 163 0 0 0 255 183 91 82 181 39 63 173 10 255 102 0 251 0 13 0 222 131 127 247 155 127 47 75 0 91 247 0 182 156 0 73 0 64 227 73 227 78 117 229 73 67 118 1 120 232 237 0 0 205 0 137 69 78 185 129 12 84 130 84 43 178 163 154 72 255 0 0 80 1 177 174 1 217 10 33 0 45 144 200 192 120 82 164 0 0 175 13 84 237 114 96 0 55 30 100 77 120 108 48 0 133 2 0 159 96 65 182 0 128 222 20 55 0 220 51 16 40 68 143 144 26 148 227 120 32 145 120 187 0 114 12 233 60 71 139 153 1 217 140 7 140 104 228 85 68 153 81 67 140 114 128 210 68 154 164 243 197 223 2 227 95 31 254 248 158 2 59 0 189 1 213 252 58 244 153 48 138 55 195 61 122 223 111 52 121 0 1 141 251 241 161 224 27 119 128 129 0 115 58 128 45 146 9 29 252 244 104 31 59 112 234 19 59 78 223 189 194 255 95 12 3 84 250 122 174 132 135 7 30 165 73 205 236 27 85 122 138 195 222 61 141 223 45 239 8 213 61 54 15 24 68 160 128 127 107 141 182 127 239 175 69 140 25 245 61 230 255 36 55 30 55 73 39 61 214 37 252 39 202 147 248 210 123 220 29 150 227 55 107 142 139 99 135 144 72 248 19 169 113 2 250 225 78 67 140 159 189 136 240 158 124 136 34 198 6 170 4 141 223 191 198 116 48 17 72 64 126 50 19 186 253 217 48 77 255 56 255 231 245 146 231 0 42 31 207 56 157 119 6 59 80 32 154 179 39 191 56 62 75 74 253 58 198 240 69 113 41 192 181 223 34 132 64 32 151 90 14 153 23 205 135 0 243 244 202 240 20 100 77 55 0 64 4 96 191 108 73 92 102 194 130 225 212 159 217 36 204 209 157 234 239 106 220 245 125 116 245 51 102 250 61 228 241 147 77 250 38 86 216 54 27 214 140 107 217 254 92 131 123 30 38 18 74 190 48 65 83 89 202 70 177 52 22 177 95 252 216 198 146 227 241 188 177 255 83 87 188 172 74 191 225 38 190 214 200 204 63 251 118 91 181 213 47 219 242 252 38 47 223 118 70 248 253 159 242 53 61 62 142 79 99 53 250 110 61 175 198 0 178 250 140 16 249 28 240 214 16 196 164 85 28 254 0 226 180 46 117 75 230 66 228 19 184 80 14 248 81 58 175 103 33 45 44 175 158 180 101 98 22 171 92 75 32 240 79 143 190 207 162 54 126 95 143 87 245 34 73 90 221 141 230 44 121 100 172 230 193 158 155 111 207 252 82 196 88 169 102 20 164 89 96 205 70 136 230 127 251 242 175 15 77 86 71 226 253 190 45 225 127 231 250 215 255 90 183 24 94 80 242 189 199 88 205 189 223 156 225 141 61 70 27 125 85 182 252 27 253 248 164 100 255 193 211 72 44 149 15 126 109 246 31 106 255 243 125 159 107 148 101 205 245 198 239 127 61 95 103 8 227 61 242 171 191 166 12 146 191 147 255 200 3 119 30 76 14 141 43 249 252 248 163 192 190 128 244 24 111 247 215 227 0 178 55 109 196 124"
var array=Array.from(string.split(" "), x => Number(x))



function assemble_png(u_in){
	var LEN = 16;
	var key = "0000000000000000";
	var shifter;
	if(u_in.length == LEN){
	key = u_in;
				}
	var result = [];
	for(var i = 0; i < LEN; i++){
		shifter = key.charCodeAt(i) - 48;
		for(var j = 0; j < (array.length / LEN); j ++){
			result[(j * LEN) + i] = array[(((j + shifter) * LEN) % array.length) + i]
			}
		}
	while(result[result.length-1] == 0){
		result = result.slice(0,result.length-1);
			}
		console.log(result)
	//document.getElementById("Area").src = "data:image/png;base64," + btoa(String.fromCharCode.apply(null, new Uint8Array(result)));
				return false;
			}


const header= [137, 80, 78, 71, 13, 10, 26, 10,0,0,0,13,73,72,68,82]
 
function findIndex(num,index){
let a=0
 array.map((o,i)=>{

if(num==o&&i%16==index){
	a=i
}
 })
 return a
}
let ans=[]
for (let i=0;i<header.length;i++){

	const a=findIndex(header[i],i)
	const r=Math.floor(a/16)
	const c=String.fromCharCode(r+48)
	ans.push(c)
}


console.log(ans)


```
We will get the following result
```
[
  '4', '5', '4',  '9',
  '6', '1', '8',  '5',
  'Q', 'P', '\\', '1',
  '2', '4', '9',  '5'
]

```
the `'Q','P','\\'` are weird. Therefore, I guess there are more than one acceptable results when I try to look up the bytes. I print all the possible result for each number in the result.

```
[ 64 ]
[ 81 ]
[ 50, 66 ]
[ 147 ]
[ 100 ]
[ 21 ]
[ 134 ]
[ 87 ]
[ 24, 40, 536 ]
[ 89, 105, 121, 521 ]
[ 10, 26, 714 ]
[ 27 ]
[ 44 ]
[ 77 ]
[ 158 ]
[ 95 ]
```
As I guess, there are more than one possible choice, and the weird ones are those with more than one result.
Since, there are not many choices, I simply test each to find out the number.

The result is `4549618526012495`

After typing the key, I than get a PNG image. The image is a QR code. 
![](https://i.imgur.com/9EaS1aW.png)

Scan the code and get the flag
`picoCTF{cfbdafe5a65de4f32cce2e81e8c14a39`
