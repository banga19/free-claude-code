"""Claude model-name helpers shared outside the core package."""

ADAPTIVE_THINKING_MODELS = frozenset(
    {
        "claude-fable-5",
        "claude-mythos-5",
    }
)


def is_adaptive_thinking_model(model_name: str | None) -> bool:
    """Return whether a Claude model requires adaptive thinking."""
    if not model_name:
        return False
    return model_name.lower() in ADAPTIVE_THINKING_MODELS
