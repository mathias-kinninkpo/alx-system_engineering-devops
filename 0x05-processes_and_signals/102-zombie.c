#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - creates an infinite loop to make the program hang
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - creates 5 zombie processes
 * Return: 0 on success
 */
int main(void)
{
	int i;
	pid_t z_pid;

	for (i = 0; i < 5; i++)
	{
		z_pid = fork();
		if (!z_pid)
			return (0);
		printf("Zombie process created, PID: %d\n", z_pid);
	}

	infinite_while();
	return (0);
}
