#include "binary_trees.h"
/**
 * binary_tree_insert_left -  Inserts a node as a left-child of
 *                           of another in a binary tree.
 * @parent: pointer to the parent node of the node to create.
 * @value: value to put in the new node.
 *
 * Return: pointer to the new node, or NULL on failure
 */
binary_tree_t *binary_tree_insert_left(binary_tree_t *parent, int value)
{
	binary_tree_t *new_n;

	if (!parent)
		return (NULL);
	new_n = malloc(sizeof(binary_tree_t));
	if (!new_n)
		return (NULL);
	new_n->parent = parent;
	new_n->n = value;
	new_n->left = parent->left;
	new_n->right = NULL;
	if (parent->left)
		parent->left->parent = new_n;
	parent->left = new_n;
	return (new_n);
}
