# -*- coding: utf-8 -*-
"""The tracing types class in agentscope."""
from opentelemetry.semconv._incubating.attributes import (
    gen_ai_attributes as GenAIAttributes,
)


class SpanAttributes:
    """The span attributes."""

    # GenAI Common Attributes
    GEN_AI_CONVERSATION_ID = GenAIAttributes.GEN_AI_CONVERSATION_ID
    """The gen ai conversation ID."""

    GEN_AI_OPERATION_NAME = GenAIAttributes.GEN_AI_OPERATION_NAME
    """The gen ai operation name."""

    # Compatibility: GEN_AI_PROVIDER_NAME was removed in newer versions
    GEN_AI_PROVIDER_NAME = getattr(GenAIAttributes, "GEN_AI_PROVIDER_NAME", "gen_ai.system")
    """The gen ai provider name."""

    # GenAI Request Attributes
    GEN_AI_REQUEST_MODEL = GenAIAttributes.GEN_AI_REQUEST_MODEL
    """The gen ai request model."""

    GEN_AI_REQUEST_TEMPERATURE = GenAIAttributes.GEN_AI_REQUEST_TEMPERATURE
    """The gen ai request temperature."""

    GEN_AI_REQUEST_TOP_P = GenAIAttributes.GEN_AI_REQUEST_TOP_P
    """The gen ai request top_p."""

    GEN_AI_REQUEST_TOP_K = GenAIAttributes.GEN_AI_REQUEST_TOP_K
    """The gen ai request top_k."""

    GEN_AI_REQUEST_MAX_TOKENS = GenAIAttributes.GEN_AI_REQUEST_MAX_TOKENS
    """The gen ai request max_tokens."""

    GEN_AI_REQUEST_PRESENCE_PENALTY = (
        GenAIAttributes.GEN_AI_REQUEST_PRESENCE_PENALTY
    )
    """The gen ai request presence_penalty."""

    GEN_AI_REQUEST_FREQUENCY_PENALTY = (
        GenAIAttributes.GEN_AI_REQUEST_FREQUENCY_PENALTY
    )
    """The gen ai request frequency_penalty."""

    GEN_AI_REQUEST_STOP_SEQUENCES = (
        GenAIAttributes.GEN_AI_REQUEST_STOP_SEQUENCES
    )
    """The gen ai request stop_sequences."""

    GEN_AI_REQUEST_SEED = GenAIAttributes.GEN_AI_REQUEST_SEED
    """The gen ai request seed."""

    # GenAI Response Attributes
    GEN_AI_RESPONSE_ID = GenAIAttributes.GEN_AI_RESPONSE_ID
    """The gen ai response ID."""

    GEN_AI_RESPONSE_FINISH_REASONS = (
        GenAIAttributes.GEN_AI_RESPONSE_FINISH_REASONS
    )
    """The gen ai response finish reasons."""

    # GenAI Usage Attributes
    GEN_AI_USAGE_INPUT_TOKENS = GenAIAttributes.GEN_AI_USAGE_INPUT_TOKENS
    """The gen ai usage input tokens."""

    GEN_AI_USAGE_OUTPUT_TOKENS = GenAIAttributes.GEN_AI_USAGE_OUTPUT_TOKENS
    """The gen ai usage output tokens."""

    # GenAI Message Attributes
    # Compatibility: These attributes may not exist in newer versions
    GEN_AI_INPUT_MESSAGES = getattr(GenAIAttributes, "GEN_AI_INPUT_MESSAGES", "gen_ai.input.messages")
    """The gen ai input messages."""

    GEN_AI_OUTPUT_MESSAGES = getattr(GenAIAttributes, "GEN_AI_OUTPUT_MESSAGES", "gen_ai.output.messages")
    """The gen ai output messages."""

    # GenAI Agent Attributes
    GEN_AI_AGENT_ID = GenAIAttributes.GEN_AI_AGENT_ID
    """The gen ai agent ID."""

    GEN_AI_AGENT_NAME = GenAIAttributes.GEN_AI_AGENT_NAME
    """The gen ai agent name."""

    GEN_AI_AGENT_DESCRIPTION = GenAIAttributes.GEN_AI_AGENT_DESCRIPTION
    """The gen ai agent description."""

    # Compatibility: GEN_AI_SYSTEM_INSTRUCTIONS was renamed to GEN_AI_SYSTEM
    GEN_AI_SYSTEM_INSTRUCTIONS = getattr(GenAIAttributes, "GEN_AI_SYSTEM_INSTRUCTIONS", getattr(GenAIAttributes, "GEN_AI_SYSTEM", "gen_ai.system"))
    """The gen ai system instructions."""

    # GenAI Tool Attributes
    GEN_AI_TOOL_CALL_ID = GenAIAttributes.GEN_AI_TOOL_CALL_ID
    """The gen ai tool call ID."""

    GEN_AI_TOOL_NAME = GenAIAttributes.GEN_AI_TOOL_NAME
    """The gen ai tool name."""

    GEN_AI_TOOL_DESCRIPTION = GenAIAttributes.GEN_AI_TOOL_DESCRIPTION
    """The gen ai tool description."""

    GEN_AI_TOOL_CALL_ARGUMENTS = "gen_ai.tool.call.arguments"
    """The gen ai tool call arguments."""

    GEN_AI_TOOL_CALL_RESULT = "gen_ai.tool.call.result"
    """The gen ai tool call result."""

    GEN_AI_TOOL_DEFINITIONS = "gen_ai.tool.definitions"
    """The gen ai tool definitions."""

    # GenAI Embedding Attributes
    GEN_AI_EMBEDDINGS_DIMENSION_COUNT = "gen_ai.embeddings.dimension.count"
    """The gen ai embeddings dimension count."""

    # AgentScope Extended Attributes
    AGENTSCOPE_FORMAT_TARGET = "agentscope.format.target"
    """The agentscope format target."""

    AGENTSCOPE_FORMAT_COUNT = "agentscope.format.count"
    """The count of formatted messages in the result."""

    AGENTSCOPE_FUNCTION_NAME = "agentscope.function.name"
    """The agentscope function name."""

    AGENTSCOPE_FUNCTION_INPUT = "agentscope.function.input"
    """The agentscope function input."""

    AGENTSCOPE_FUNCTION_OUTPUT = "agentscope.function.output"
    """The agentscope function output."""


class OperationNameValues:
    """The operation name values."""

    FORMATTER = "format"
    """The formatter operation name."""

    INVOKE_GENERIC_FUNCTION = "invoke_generic_function"
    """The invoke generic function operation name."""

    # Compatibility: GenAiOperationNameValues may not exist in newer versions
    _operation_values = getattr(GenAIAttributes, "GenAiOperationNameValues", None)
    
    CHAT = _operation_values.CHAT.value if _operation_values and hasattr(_operation_values, "CHAT") else "chat"
    """The chat operation name."""

    INVOKE_AGENT = _operation_values.INVOKE_AGENT.value if _operation_values and hasattr(_operation_values, "INVOKE_AGENT") else "invoke_agent"
    """The invoke agent operation name."""

    EXECUTE_TOOL = _operation_values.EXECUTE_TOOL.value if _operation_values and hasattr(_operation_values, "EXECUTE_TOOL") else "execute_tool"
    """The execute tool operation name."""

    EMBEDDINGS = _operation_values.EMBEDDINGS.value if _operation_values and hasattr(_operation_values, "EMBEDDINGS") else "embeddings"
    """The embeddings operation name."""


class ProviderNameValues:
    """The provider name values."""

    DASHSCOPE = "dashscope"
    """The dashscope provider name."""

    OLLAMA = "ollama"
    """The ollama provider name."""

    # Compatibility: GenAiProviderNameValues may not exist in newer versions
    _provider_values = getattr(GenAIAttributes, "GenAiProviderNameValues", None)
    
    DEEPSEEK = _provider_values.DEEPSEEK.value if _provider_values and hasattr(_provider_values, "DEEPSEEK") else "deepseek"
    """The deepseek provider name."""

    OPENAI = _provider_values.OPENAI.value if _provider_values and hasattr(_provider_values, "OPENAI") else "openai"
    """The openai provider name."""

    ANTHROPIC = _provider_values.ANTHROPIC.value if _provider_values and hasattr(_provider_values, "ANTHROPIC") else "anthropic"
    """The anthropic provider name."""

    GCP_GEMINI = _provider_values.GCP_GEMINI.value if _provider_values and hasattr(_provider_values, "GCP_GEMINI") else "gcp_gemini"
    """The gcp gemini provider name."""

    MOONSHOT = "moonshot"
    """The moonshot provider name."""

    AZURE_AI_OPENAI = _provider_values.AZURE_AI_OPENAI.value if _provider_values and hasattr(_provider_values, "AZURE_AI_OPENAI") else "azure_ai_openai"
    """The azure openai provider name."""

    AWS_BEDROCK = _provider_values.AWS_BEDROCK.value if _provider_values and hasattr(_provider_values, "AWS_BEDROCK") else "aws_bedrock"
    """The aws bedrock provider name."""
