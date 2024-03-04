# 0x03. Queuing System in JS


This directory contains Node.js projects focused on implementing queuing systems using Redis and Kue. Each task explores different aspects of setting up queues, processing jobs asynchronously, and managing job priorities.

## Table of Contents

- [Task Descriptions](#task-descriptions)
- [Overview Concepts](#overview-concepts)
- [Requirements](#requirements)
- [Setup](#setup)
- [Usage](#usage)

## Task Descriptions

- **Task 0: [README.md](README.md), [dump.rdb](dump.rdb)** -  Installed a redis instance, Initializing the project with a README file and copied the dump.rdb from the redis-6.0.10 directory into the root of the Queuing project.
- **Task 1: [0-redis_client.js](0x03-queuing_system_in_js/0-redis_client.js)** - Creating a Redis client and setting up basic operations.
- **Task 2: [1-redis_op.js](0x03-queuing_system_in_js/1-redis_op.js)** - Implementing Redis operations for setting and getting data.
- **Task 3: [2-redis_op_async.js](0x03-queuing_system_in_js/2-redis_op_async.js)** - Performing Redis operations asynchronously using async/await.
- **Task 4: [4-redis_advanced_op.js](0x03-queuing_system_in_js/4-redis_advanced_op.js)** - Performing advanced Redis operations such as pipelining and transactions.
- **Task 5: [5-subscriber.js](0x03-queuing_system_in_js/5-subscriber.js), [5-publisher.js](0x03-queuing_system_in_js/5-publisher.js)** - Implementing a simple publisher/subscriber model using Redis.
- **Task 6: [6-job_creator.js](0x03-queuing_system_in_js/6-job_creator.js)** - Creating jobs in a Kue queue for processing asynchronously.
- **Task 7: [6-job_processor.js](0x03-queuing_system_in_js/6-job_processor.js)** - Processing jobs in a Kue queue to perform specific tasks.
- **Task 8: [7-job_creator.js](0x03-queuing_system_in_js/7-job_creator.js)** - Creating jobs in a Kue queue to handle notifications.
- **Task 9: [7-job_processor.js](0x03-queuing_system_in_js/7-job_processor.js)** - Processing notification jobs in a Kue queue to send notifications.
- **Task 10: [8-job.js](0x03-queuing_system_in_js/8-job.js)** - Creating jobs in a Kue queue to process notifications.
- **Task 11: [8-job.test.js](0x03-queuing_system_in_js/8-job.test.js)** - Writing tests for the push notification job creation function using Mocha and Chai.
- **Task 12: [9-stock.js](0x03-queuing_system_in_js/9-stock.js)** - Implementing a web server with Express to manage product stock using Redis and Kue.
- **Task 13: [100-seat.js](0x03-queuing_system_in_js/100-seat.js)** - Developing an Express server with routes to reserve seats using Redis and Kue.

## Overview Concepts

The tasks in this directory cover the following queuing system concepts:

- Setting up Kue queues and processing jobs asynchronously.
- Implementing job creation and processing functions using Kue.
- Writing tests for job creation functions using Mocha and Chai.
- Managing product stock and reservations using Redis and Express.
- Implementing seat reservation system with Redis and Kue.

## Requirements

- Node.js
- npm (Node Package Manager)
- Redis server

## Setup

1. Install Node.js:

```bash
sudo apt update
sudo apt install nodejs
```

2. Install npm:

```bash
sudo apt install npm
```

3. Install Redis server:

```bash
sudo apt install redis-server
```

4. Install project dependencies:

```bash
cd 0x03-queuing_system_in_js
npm install
```

## Usage

- To run the server for Task 12:

```bash
npm run dev 9-stock.js
```

- To run the server for Task 13:

```bash
npm run dev 100-seat.js
```
