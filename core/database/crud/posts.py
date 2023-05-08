import imp
from typing import List, Literal, Optional
from ..models.posts import Category, Post, PostMeta


class PostsCRUD:
    """
    Database Operations with `Posts & Categories`.

    Made for managers
    """
    @classmethod
    def get_posts(self, limit: Optional[int]) -> List[Post]:
        """
        Get's list of posts with available filters
        """
        query: List[Post] = Post.select().limit(limit).order_by(Post.created_at.desc())

        return query

    @classmethod
    def get_category_posts(self, category_slug: str) -> List[Post]:
        """
        Get's list of posts from category
        """
        category = self.get_category(category_slug)
        if not category:
            return []

        query: List[Post] = Post.select().where(Post.category_id == category.id).order_by(Post.created_at.desc())

        return query

    @classmethod
    def get_post(self, slug: str) -> Optional[Post]:
        """
        Get's 1 post from list of posts by slug

        Args:
            slug (str): Slug of the post, or link string
        """
        query: Optional[Post] = Post.get_or_none(Post.slug == slug)

        return query

    @classmethod
    def find_post(self, query: str) -> List[Post]:
        """
        This method was made for finding post to make search

        Args:
            query (str): Query string which can be post meta, title or content
        """
        query: List[Post] = Post.select().where(
            (Post.title % query) or (Post.content % query))

        if len(query):
            return query

        meta_query: List[PostMeta] = PostMeta.select().where(
            PostMeta.name % query)

        return list(map(lambda c: self.get_post(c.post.id), meta_query))

    @classmethod
    def get_categories(self, limit: Optional[int], order: Literal["asc", "desc"]) -> List[Category]:
        """
        Get's list of categories with available filters
        """
        query: List[Category] = Category.select().limit(limit).order(order)

        return query
    
    @classmethod
    def get_category(self, slug: str) -> Optional[Category]:
        """
        Get's 1 post category from list of post categories by slug

        Args:
            slug (str): Slug of the post category - Humaized URL string
        """
        query = Post.get_or_none(Post.slug == slug)

        return query
    
    @classmethod
    def find_category(self, query: str) -> List[Category]:
        """
        This method was made for finding post category to make search

        Args:
            query (str): Query string which can be title, description of post category
        """
        query: List[Category] = Category.select().where((Category.title % query) or (Category.description % query))

        return query