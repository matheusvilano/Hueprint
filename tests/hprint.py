import unittest
import sys
from io import StringIO
from hueprint import sprint, cprint, eprint, wprint, nprint, iprint, EEffect, EColour


class HueprintTest(unittest.TestCase):

	@property
	def _test_text(self) -> str:
		"""The test text to use."""
		return "Test"

	def _readline(self) -> str:
		"""Get the last line of the console."""
		return self._captured_output.getvalue().strip()

	def setUp(self) -> None:
		"""Constructor-like method for the Hueprint test case. This replaces `__init__` and is called automatically after each test."""
		super().__init__()
		self._captured_output = StringIO()
		sys.stdout = self._captured_output

	def tearDown(self) -> None:
		"""Destructor-like method for the Hueprint test case. This replaces `__del__` and is called automatically after each test."""
		super().tearDown()

	def test_modifiers(self):
		cprint(self._test_text, EColour.LIGHT_GREEN, EEffect.ITALIC) 
		expected_text = EEffect.ITALIC.value + EColour.LIGHT_GREEN.value + self._test_text + EColour.NONE.value
		actual_text = self._readline()
		self.assertEqual(expected_text, actual_text, "The text printed to the console does not match the expected text.")
