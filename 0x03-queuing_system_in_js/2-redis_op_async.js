import redis from 'redis';
// Asycn Implemnetation
import { promisify } from 'util';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err}`);
});

// Function to set a new school value in Redis
const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, redis.print);
};

// Function to display the value for a given school name
const displaySchoolValue = async (schoolName) => {
  const asyncGet = promisify(client.get).bind(client);
  try {
    const reply = await asyncGet(schoolName);
    console.log(reply);
  } catch (error) {
    console.error(`Error retrieving value for ${schoolName}: ${error}`);
  }
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
