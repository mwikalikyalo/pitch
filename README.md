# Pitch-hub
#### By Ruweydha Abdinoor.
## Description
A website where a user can be able to view pitches from other people, comment on pitches, see pitches from any category and submit a pitch in any category. The app has a user authentication system where only registered users can post a pitch and comment on other pitches. They can pick the category on the navbar link
## Setup and Installation

1. Clone the repository


2. Navigate to project folder

```bash
cd Pitch-hub
```

3. Create a virtual environment
```
python3 -m venv <name>
```

4. Activate the virtual environment

source <name>/bin/activate

5. Install dependencies

```
pip intall -r requirements.txt
```

6. Create the .env variables in the root folder
```bash
touch .env
```
Create the environment  variables

export SECRET_KEY='<Your Secret Key>'

7. Load the environment variables

```bash
source .env
```
4. Grant the python executable permissions

```
chmod +x start.sh
```
5. Run the application

```
./start.sh
 ```

## Requirements
* Either a computer,phone,tablet or an Ipad
* An access to the Internet

## Known Bugs
None at the moment.
## Technologies Used
* Flask
* HTML
* Bootstrap

    
## Support and contact details
LinkedIn - [Ruweydha Abdinoor](https://www.linkedin.com/in/ruweydha-abdinoor-859921224/) 
### License
MIT License
​
Copyright (c) [2022] [Ruweydha Abdinoor]
​
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
​
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
​
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.