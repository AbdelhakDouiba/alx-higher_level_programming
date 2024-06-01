#include "lists.h"

/**
*check_cycle - checks if a singly linked list has a cycle in it.
*@list: singly linked list
*
*Return: 0 if there is no cycle, 1 if there is a cycle
*/

int check_cycle(listint_t *list)
{
	listint_t *tmp = list;

	while (tmp != NULL)
	{
		if (tmp->next == tmp)
			return (1);
		tmp = tmp->next;
	}
	return (0);
}