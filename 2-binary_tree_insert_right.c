#include "binary_trees.h"
/**
 * binary_tree_insert_right -  Insert a node as the right-child
 *                            of another in a binary tree.
 * @parent: pointer to the parent node of the node to create.
 * @value: value to put in the new node.
 *
 * Return: pointer to the new node, or NULL on failure
 */
binary_tree_t *binary_tree_insert_right(binary_tree_t *parent, int value)
{
	binary_tree_t *new_n;

	if (!parent)
		return (NULL);
	new_n = malloc(sizeof(binary_tree_t));
	if (!new_n)
		return (NULL);
	new_n->parent = parent;
	new_n->n = value;
	new_n->left = NULL;
	new_n->right = parent->right;
	if (parent->right)
		parent->right->parent = new_n;
	parent->right = new_n;
	return (new_n);
}
