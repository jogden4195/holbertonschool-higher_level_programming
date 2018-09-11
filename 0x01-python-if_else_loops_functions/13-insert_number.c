#include "lists.h"

/**
 * insert_node - inserts anumber into a sorted singly linked list
 * @head: first node in the list
 * @number: number we are trying to insert
 *
 * Return: address of the new node or NULL if failure
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *next_node;
	listint_t *after_new;

	if (head == NULL)
		return (NULL);
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	if (*head == NULL)
	{
		new_node->next = *head;
		*head = new_node;
		return (*head);
	}
	next_node = *head;
	while (next_node && next_node->n < number)
	{
		if (next_node->next->n > number)
			break;
		next_node = next_node->next;
	}
	after_new = next_node->next;
	next_node->next = new_node;
	new_node->next = after_new;
	return (new_node);
}
