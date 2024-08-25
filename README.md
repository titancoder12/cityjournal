# **CityJournal**

Project that I made to practice making using the Django Rest API Framework. 


# **Description**

**CityJournal is an application that allows for users to take a photo and record the location where the photo was taken. Users record journal entries for each location, creating a record of places they have been to.**


# **API Documentation**

API path is at localhost:8000/api


## **/journalentry**

**Methods:**

Add an entry (POST)

View an entry (GET)

**View an entry (GET)**


<table>
  <tr>
   <td>Input
   </td>
   <td>Output
   </td>
  </tr>
  <tr>
   <td>id: Integer
   </td>
   <td>title: String,
<p>
location: Array,
<p>
body: String,
<p>
entry_id: Integer
<p>
user_id: Integer
   </td>
  </tr>
</table>


**Add an entry (POST)**


<table>
  <tr>
   <td>Input
   </td>
   <td>Output
   </td>
  </tr>
  <tr>
   <td>title: String,
<p>
location: Array,
<p>
body: String,
<p>
user_id: Integer
   </td>
   <td>title: String,
<p>
location: Array,
<p>
body: String,
<p>
user_id: Integer
   </td>
  </tr>
</table>


**An authorization token of the current user must be provided for all GET and POST requests. The token must also be associated with the same user as user_id.**

**id** (integer) - Id of the entry

**entry_id **(Integer) - Id of the entry

**user_id** (Integer) - The id of the user creating the entry

**title** (String) - Title of the entry

**location** (Array) - Location associated with the entry in the format [Latitude, Longitude] where Latitude and Longitude are Decimals.

**body** (String) - Text associated with the entry

**images** (Array) - Array of image_ids


## **/image**

**Methods:**

View image (GET)

Add image (POST)

**Add image (POST)**


<table>
  <tr>
   <td>Input
   </td>
   <td>Output
   </td>
  </tr>
  <tr>
   <td>image: BLOB,
<p>
entry_id: Integer
   </td>
   <td>image_id: Integer
   </td>
  </tr>
</table>


**View image (GET)**


<table>
  <tr>
   <td>Input
   </td>
   <td>Output
   </td>
  </tr>
  <tr>
   <td>entry_id: Integer
   </td>
   <td>image: BLOB,
<p>
user_id: Integer
   </td>
  </tr>
</table>


**An authorization token of the current user must be provided for all POST requests. The token must also be associated with the same user as user_id.**

**image** (BLOB) - Image to add to database

**entry_id** (Integer) - Id of the entry to be associated with the image

**image_id** (Integer) - Id of newly added image


## **/journalentries**

**Methods:**

View entries (GET)

Add an entry (POST)

**View entries (GET)**


<table>
  <tr>
   <td>Input
   </td>
   <td>Output
   </td>
  </tr>
  <tr>
   <td>limit: Integer (Default=all)
   </td>
   <td><strong>entries:</strong>
<p>
    title: String,
<p>
    location: Array,
<p>
    body: String,
<p>
    image: BLOB,
<p>
    entry_id: Integer,
<p>
    user_id: Integer,
<p>
    .
<p>
    .
<p>
    .
   </td>
  </tr>
</table>


**Objects are returned in order of time added to database.**

**Must be logged in/Authenticated.**

**limit** (Integer, default=all) - Number of entries to return

**user_id **(Integer) - Id of the user

**entry_id **(Integer) - Id of the entry

**entries** (Dictionary) - Dictionary. The first and only row contains a value containing a list of all entries, where each individual entry is another dictionary.

**title** (String) - Title of the entry

**location** (Array) - Location associated with the entry in the format [Latitude, Longitude] where Latitude and Longitude are Decimals.

**body** (String) - Text associated with the entry

**images** (Array) - Array of image_ids


## **/register**

**Methods:**

Register (POST)

**Register (POST)**


<table>
  <tr>
   <td>Input
   </td>
   <td>Output
   </td>
  </tr>
  <tr>
   <td>username: String,
<p>
email: String,
<p>
password: String
   </td>
   <td>username: String,
<p>
email: String,
<p>
password: String
   </td>
  </tr>
</table>


**username** (String) - Username of the user-to-be

**email **(String) - Email of the user-to-be

**password** (String) - Password of the user-to-be


## **/login**

**Methods:**

Register (POST)

**Register (POST)**


<table>
  <tr>
   <td>Input
   </td>
   <td>Output
   </td>
  </tr>
  <tr>
   <td>username: String,
<p>
password: String
   </td>
   <td>token: Integer
   </td>
  </tr>
</table>


**username** (String) - Username of the user-to-be

**password** (String) - Password of the user-to-be

**token **(Integer) - User token for authentication \



## **/logout**

**Methods:**

Register (POST)

**Register (POST)**


<table>
  <tr>
   <td>Input
   </td>
   <td>Output
   </td>
  </tr>
  <tr>
   <td>Include token in header
   </td>
   <td>
   </td>
  </tr>
</table>


