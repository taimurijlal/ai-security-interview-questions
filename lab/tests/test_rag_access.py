"""Q3: document-level access control enforced at retrieval time."""

import unittest

from secure_agent.rag import retrieve

QUERY = "What are the salary bands?"


class RagAccessTest(unittest.TestCase):
    def test_vulnerable_retrieval_leaks_across_departments(self):
        self.assertIn("hr-001", [d.doc_id for d in retrieve(QUERY, "alice", enforce_acl=False)])

    def test_secure_retrieval_filters_other_departments(self):
        self.assertNotIn("hr-001", [d.doc_id for d in retrieve(QUERY, "alice", enforce_acl=True)])

    def test_authorised_user_still_gets_the_document(self):
        self.assertIn("hr-001", [d.doc_id for d in retrieve(QUERY, "bob", enforce_acl=True)])

    def test_unknown_user_sees_only_public_documents(self):
        docs = retrieve("office hours refund salary", "mallory", enforce_acl=True)
        self.assertTrue(all(d.department == "public" for d in docs))


if __name__ == "__main__":
    unittest.main()
