import asyncio

# Async function that simulates a task with delay
async def task_one():
    print("Task One started")
    await asyncio.sleep(2)  # Simulating a time-consuming task
    print("Task One completed")

# Another async function
async def task_two():
    print("Task Two started")
    await asyncio.sleep(1)
    print("Task Two completed")

# Main function to run the tasks concurrently
async def main():
    # Running both tasks concurrently
    await asyncio.gather(task_one(), task_two())

# Running the main function
asyncio.run(main())
