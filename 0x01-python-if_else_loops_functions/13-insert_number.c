#include "lists.h"

/**
 * insert_node - inserts a node in a singly linked list
 * @head: already existing elements in linked list
 * @number: number to add to the new node
 * Return: new linked list
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *prev = NULL;
	listint_t *cur = *head;
	listint_t *t_new;

	t_new = malloc(sizeof(listint_t));
	if (t_new == NULL)
		return (NULL);

	t_new->n = number;

	while (cur && cur->n < number)
	{
		prev = cur;
		cur = cur->next;
	}

	t_new->next = cur;
	if (prev)
		prev->next = t_new;
	else
		*head = t_new;
	return (t_new);
}
