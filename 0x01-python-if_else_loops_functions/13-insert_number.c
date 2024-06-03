#include <stdlib.h>
#include "lists.h"
/**
*insert_node - inserts a number into a sorted singly linked list.
*@head: a pointer to the head of the list
*@number: the data to be inserted
*
*Return: the list
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp = *head, *node;

	node = (listint_t *)malloc(sizeof(listint_t));
	if (node == NULL)
		return (NULL);
	node->n = number;
	if (tmp->n > number || *head == NULL)
	{
		node->next = *head;
		*head = node;
		return (*head);
	}
	while (tmp->next != NULL && tmp->next->n < number)
	{
		tmp = tmp->next;
	}
	node->next = tmp->next;
	tmp->next = node;
	return (*head);
}
