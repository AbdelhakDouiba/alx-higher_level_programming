#include <stdlib.h>
#include "lists.h"

/**
*is_palindrome - checks if a singly linked list is a palindrome.
*@head: the head of the list.
*
*Return: 0 if it is not a palindrome, 1 if it is a palindrome
*/
int is_palindrome(listint_t **head)
{
	int *list, len = 0, i, j;
	listint_t *tmp;

	if (head == NULL || *head == NULL)
		return (0);
	for (tmp = *head; tmp != NULL; tmp = tmp->next)
		len++;
	if (len == 1)
		return (1);
	list = (int *)malloc(sizeof(int) * len);
	if (list == NULL)
		return (0);
	tmp = *head;
	for (i = 0; i < len; i++)
	{
		list[i] = tmp->n;
		tmp = tmp->next;
	}
	i = 0;
	j = len - 1;
	while (i < j)
	{
		if (list[i] != list[j])
		{
			free(list);
			return (0);
		}
		i++;
		j--;
	}
	free(list);
	return (1);
}
