## SQL Exercise

<br />

**Set Up Dog Shelter Database: CREATE DATABASE**  
Animals 4 Homes is getting ready to open and help dogs find loving homes.  

To get started, we need to set up a SQL database to store and manage each dog as
they come in and get adopted.  

First, we need to create a database for our data. We’ll name it pet_adoption using the following SQL statement:  

```sql
CREATE DATABASE pet_adoption;
```

Creating a database doesn’t automatically set it as the active database, so now let’s select the pet_adoption database with the USE command:  

```sql
USE pet_adoption;
```

Next, we need to set up the tables that will store our data.  

For this project, let’s create just two tables: animals and adoptions.  

**Table #1: A Table for Animals: CREATE TABLE & UUID**  
The first table, animals, will maintain a list of the dogs that come through our shelter.  

Create the animal table with the following command:  

```sql
CREATE TABLE animals (id UUID NOT NULL, name STRING, breed STRING, color STRING, gender STRING, status INTEGER);
```

**Table #2: The List of Adoptions: TIMESTAMP**

The second table will be named adoptions. It will be used to track all adoption
transactions.

Create this adoptions table using the following command:  

```sql
CREATE TABLE adoptions (animal_id UUID NOT NULL, name STRING, contact STRING, date TIMESTAMP);
```

**Verify Database Setup: SHOW TABLES & COLUMNS**

Run this command to get the list of tables in the current database and check that we
have both the animals table and the adoptions table:

```sql
SHOW TABLES;
```

If you see both tables, then you can run these two statements to make sure that the
columns of each are correct:

```sql
SHOW COLUMNS FROM animals;
SHOW COLUMNS FROM adoptions;
```

Now that our database schema looks good, we’re ready to start accepting dogs at our
shelter.

**Add Dogs to Database: INSERT**

They are eager to check in and look cute to visitors, so let’s add them to the system quickly. We can do this using an INSERT statement on the animals table that looks like the following:  

```sql
INSERT INTO animals (id, name, breed, color, gender, status) VALUES ('89354034-20d9-4c3d-8195-3294bfd9dbc5', 'Bellyflop', 'Beagle', 'Brown', 'Male', 0);
```

**Retrieve List of Dogs: SELECT * FROM**

With the full list of dogs added to our database, we can try running some SELECT
queries to look through them. The following are some small examples of possible SQL
statements to run.

Get the full list of all properties of all dogs (defaults to a limit of 100 rows):

```sql
SELECT * FROM animals;
```

Get the breeds of all dogs:

```sql
SELECT breed FROM animals;
```

Get the names of only female dogs by including a WHERE clause:

```sql
SELECT name FROM animals WHERE gender = 'Female';
```

Get the IDs of dogs up for adoption:

```sql
SELECT id FROM animals WHERE status = 0;
```