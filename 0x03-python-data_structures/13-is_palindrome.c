#include <stdlib.h>

#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: the head of the list.
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *prev_slow = NULL;
	listint_t *second_half = NULL, *mid = NULL;
	int palindrome = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (fast && fast->next)
	{
		prev_slow = slow;
		slow = slow->next;
		fast = fast->next->next;
	}
	if (fast != NULL)
	{
		mid = slow;
		slow = slow->next;
	}
	second_half = reverse_list(&slow);
	while (second_half != NULL)
	{
		if ((*head)->n != second_half->n)
		{
			palindrome = 0;
			break;
		}
		*head = (*head)->next;
		second_half = second_half->next;
	}
	if (mid != NULL)
	{
		prev_slow->next = reverse_list(&slow);
		mid->next = slow;
	}
	else
		prev_slow->next = reverse_list(&slow);
	return (palindrome);
}

/**
 * reverse_list - reverse a list
 * @head: head of a list
 *
 * Return: the reversed list
 */
listint_t *reverse_list(listint_t **head)
{
	listint_t *prev = NULL, *current = *head, *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
	return (*head);
}
