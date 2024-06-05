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
	int len = 0, i;
	listint_t *tmp, *mid, *rev, *tmp_rev;

	if (head == NULL || *head == NULL)
		return (1);
	for (tmp = *head; tmp != NULL; tmp = tmp->next)
		len++;
	if (len == 1)
		return (1);
	mid = *head;
	for (i = 0; i < (len / 2); i++)
		mid = mid->next;
	if (len % 2 != 0)
		mid = mid->next;
	rev = mid->next;
	mid->next = NULL;
	rev = reverse_list(&rev);
	tmp = *head;
	tmp_rev = rev;
	while (tmp_rev != NULL)
	{
		if (tmp_rev->n != tmp->n)
		{
			mid->next = reverse_list(&rev);
			return (0);
		}
		tmp_rev = tmp_rev->next;
		tmp = tmp->next;
	}
	return (1);
}


/**
*reverse_list - reverse a list
*
*@head: head of a list
*
*Return: the reversed list
*/
listint_t *reverse_list(listint_t **head)
{
	listint_t *prev = NULL, *current = *head, *next;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	return (prev);
}
