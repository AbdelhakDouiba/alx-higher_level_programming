#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
*check_cycle - checks if a singly linked list has a cycle in it.
*@list: singly linked list
*
*Return: 0 if there is no cycle, 1 if there is a cycle
*/

int check_cycle(listint_t *list)
{
	listint_t *tmp = list, *step = list;

	while (tmp != NULL && tmp->next != NULL)
	{
		step = step->next->next;
		tmp = tmp->next;
		if (tmp == step)
			return (1);
	}
	return (0);
}
