#ifndef AWS_HTTP_REQUEST_RESPONSE_IMPL_H
#define AWS_HTTP_REQUEST_RESPONSE_IMPL_H

/*
 * Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License").
 * You may not use this file except in compliance with the License.
 * A copy of the License is located at
 *
 *  http://aws.amazon.com/apache2.0
 *
 * or in the "license" file accompanying this file. This file is distributed
 * on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
 * express or implied. See the License for the specific language governing
 * permissions and limitations under the License.
 */

#include <aws/http/request_response.h>

#include <aws/http/private/http_impl.h>

#include <aws/common/atomics.h>

struct aws_http_stream_vtable {
    void (*destroy)(struct aws_http_stream *stream);
    void (*update_window)(struct aws_http_stream *stream, size_t increment_size);
};

/**
 * Base class for streams.
 * There are specific implementations for each HTTP version.
 */
struct aws_http_stream {
    const struct aws_http_stream_vtable *vtable;
    struct aws_allocator *alloc;
    struct aws_http_connection *owning_connection;

    void *user_data;
    aws_http_stream_outgoing_body_fn *stream_outgoing_body;
    aws_http_on_incoming_headers_fn *on_incoming_headers;
    aws_http_on_incoming_header_block_done_fn *on_incoming_header_block_done;
    aws_http_on_incoming_body_fn *on_incoming_body;
    aws_http_on_request_end_fn *on_request_end;
    aws_http_on_stream_complete_fn *on_complete;

    struct aws_atomic_var refcount;
    bool request_handler_configured;

    int incoming_response_status;
    enum aws_http_method incoming_request_method;
    struct aws_byte_cursor incoming_request_method_str;
    struct aws_byte_cursor incoming_request_uri;
};

#endif /* AWS_HTTP_REQUEST_RESPONSE_IMPL_H */
