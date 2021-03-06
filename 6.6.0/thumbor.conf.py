################################### Logging ####################################

## Logging configuration as json
## Defaults to: None
{{- with .Env.THUMBOR_LOG_CONFIG }}
THUMBOR_LOG_CONFIG = '{{ . }}'
{{- end }}


## Log Format to be used by thumbor when writing log messages.
## Defaults to: '%(asctime)s %(name)s:%(levelname)s %(message)s'
{{- with .Env.THUMBOR_LOG_FORMAT }}
THUMBOR_LOG_FORMAT = '{{ . }}'
{{- end }}

## Date Format to be used by thumbor when writing log messages.
## Defaults to: '%Y-%m-%d %H:%M:%S'
{{- with .Env.THUMBOR_LOG_DATE_FORMAT }}
THUMBOR_LOG_DATE_FORMAT = '{{ . }}'
{{- end }}

################################################################################


################################### Imaging ####################################

## Max width in pixels for images read or generated by thumbor
## Defaults to: 0
{{- with .Env.MAX_WIDTH }}
MAX_WIDTH = {{ atoi . }}
{{- end }}

## Max height in pixels for images read or generated by thumbor
## Defaults to: 0
{{- with .Env.MAX_HEIGHT }}
MAX_HEIGHT = {{ atoi . }}
{{- end }}

## Max pixel count for images read by thumbor
## Defaults to: 75000000.0
{{- with .Env.MAX_PIXELS }}
MAX_PIXELS = {{ atoi . }}
{{- end }}

## Min width in pixels for images read or generated by thumbor
## Defaults to: 1
{{- with .Env.MIN_WIDTH }}
MIN_WIDTH = {{ atoi . }}
{{- end }}

## Min width in pixels for images read or generated by thumbor
## Defaults to: 1
{{- with .Env.MIN_HEIGHT }}
MIN_HEIGHT = {{ atoi . }}
{{- end }}

## Allowed domains for the http loader to download. These are regular
## expressions.
## Defaults to: #    [
#    ]
{{- with .Env.ALLOWED_SOURCES }}
ALLOWED_SOURCES = [
{{- range $value := (split . " ") }}
    '{{ $value }}',
{{- end }}
]
{{- end }}


## Quality index used for generated JPEG images
## Defaults to: 80
{{- with .Env.QUALITY }}
QUALITY = {{ atoi . }}
{{- end }}

## Exports JPEG images with the `progressive` flag set.
## Defaults to: True
{{- with .Env.PROGRESSIVE_JPEG }}
PROGRESSIVE_JPEG = {{ if isTrue . }}True{{ else }}False{{- end }}
{{- end }}

## Specify subsampling behavior for Pillow (see `subsampling`               in
## http://pillow.readthedocs.org/en/latest/handbook/image-file-
## formats.html#jpeg).Be careful to use int for 0,1,2 and string for "4:4:4"
## notation. Will ignore `quality`. Using `keep` will copy the original file's
## subsampling.
## Defaults to: None
{{- with .Env.PILLOW_JPEG_SUBSAMPLING }}
PILLOW_JPEG_SUBSAMPLING = '{{ . }}'
{{- end }}

## Specify quantization tables for Pillow (see `qtables`               in
## http://pillow.readthedocs.org/en/latest/handbook/image-file-
## formats.html#jpeg). Will ignore `quality`. Using `keep` will copy the
## original file's qtables.
## Defaults to: None
{{- with .Env.PILLOW_JPEG_QTABLES }}
PILLOW_JPEG_QTABLES = '{{ . }}'
{{- end }}

## Specify resampling filter for Pillow resize method.One of LANCZOS, NEAREST,
## BILINEAR, BICUBIC, HAMMING (Pillow>=3.4.0).
## Defaults to: 'LANCZOS'
{{- with .Env.PILLOW_RESAMPLING_FILTER }}
PILLOW_RESAMPLING_FILTER = '{{ . }}'
{{- end }}

## Quality index used for generated WebP images. If not set (None) the same level
## of JPEG quality will be used.
## Defaults to: None
{{- with .Env.WEBP_QUALITY }}
WEBP_QUALITY = {{ atoi . }}
{{- end }}

## Compression level for generated PNG images.
## Defaults to: 6
{{- with .Env.PNG_COMPRESSION_LEVEL }}
PNG_COMPRESSION_LEVEL = {{ atoi . }}
{{- end }}

## Indicates if final image should preserve indexed mode (P or 1) of original
## image
## Defaults to: True
{{- with .Env.PILLOW_PRESERVE_INDEXED_MODE }}
PILLOW_PRESERVE_INDEXED_MODE = {{ if isTrue . }}True{{ else }}False{{- end }}
{{- end }}

## Specifies whether WebP format should be used automatically if the request
## accepts it (via Accept header)
## Defaults to: False
{{- with .Env.AUTO_WEBP }}
AUTO_WEBP = {{ if isTrue . }}True{{ else }}False{{- end }}
{{- end }}

## Specifies whether a PNG image should be used automatically if the png image
## has no transparency (via alpha layer). WARNING: Depending on case, this is
## not a good deal. This transformation maybe causes distortions or the size
## of image can increase. Images with texts, for example, the result image
## maybe will be distorced. Dark images, for example, the size of result image
## maybe will be bigger. You have to evaluate the majority of your use cases
## to take a decision about the usage of this conf.
## Defaults to: False
{{- with .Env.AUTO_PNG_TO_JPG }}
AUTO_PNG_TO_JPG = {{ if isTrue . }}True{{ else }}False{{- end }}
{{- end }}

## Specify the ratio between 1in and 1px for SVG images. This is only used
## whenrasterizing SVG images having their size units in cm or inches.
## Defaults to: 150
{{- with .Env.SVG_DPI }}
SVG_DPI = {{ atoi . }}
{{- end }}

## Max AGE sent as a header for the image served by thumbor in seconds
## Defaults to: 86400
{{- with .Env.MAX_AGE }}
MAX_AGE = {{ atoi . }}
{{- end }}

## Indicates the Max AGE header in seconds for temporary images (images with
## failed smart detection)
## Defaults to: 0
{{- with .Env.MAX_AGE_TEMP_IMAGE }}
MAX_AGE_TEMP_IMAGE = {{ atoi . }}
{{- end }}

## Indicates whether thumbor should rotate images that have an Orientation EXIF
## header
## Defaults to: False
{{- with .Env.RESPECT_ORIENTATION }}
RESPECT_ORIENTATION = {{ if isTrue . }}True{{ else }}False{{- end }}
{{- end }}

## Ignore errors during smart detections and return image as a temp image (not
## saved in result storage and with MAX_AGE_TEMP_IMAGE age)
## Defaults to: False
{{- with .Env.IGNORE_SMART_ERRORS }}
IGNORE_SMART_ERRORS = {{ if isTrue . }}True{{ else }}False{{- end }}
{{- end }}

## Sends If-Modified-Since & Last-Modified headers; requires support from result
## storage
## Defaults to: False
{{- with .Env.SEND_IF_MODIFIED_LAST_MODIFIED_HEADERS }}
SEND_IF_MODIFIED_LAST_MODIFIED_HEADERS = {{ if isTrue . }}True{{ else }}False{{- end }}
{{- end }}

## Preserves exif information in generated images. Increases image size in
## kbytes, use with caution.
## Defaults to: False
{{- with .Env.PRESERVE_EXIF_INFO }}
PRESERVE_EXIF_INFO = {{ if isTrue . }}True{{ else }}False{{- end }}
{{- end }}

## Indicates whether thumbor should enable the EXPERIMENTAL support for animated
## gifs.
## Defaults to: True
{{- with .Env.ALLOW_ANIMATED_GIFS }}
ALLOW_ANIMATED_GIFS = {{ if isTrue . }}True{{ else }}False{{- end }}
{{- end }}

## Indicates whether thumbor should use gifsicle engine. Please note that smart
## cropping and filters are not supported for gifs using gifsicle (but won't
## give an error).
## Defaults to: False
{{- with .Env.USE_GIFSICLE_ENGINE }}
USE_GIFSICLE_ENGINE = {{ if isTrue . }}True{{ else }}False{{- end }}
{{- end }}

## Indicates whether thumbor should enable blacklist functionality to prevent
## processing certain images.
## Defaults to: False
{{- with .Env.USE_BLACKLIST }}
USE_BLACKLIST = {{ if isTrue . }}True{{ else }}False{{- end }}
{{- end }}

## Size of the thread pool used for image transformations.  The default value is
## 0 (don't use a threadpoool. Increase this if you are seeing your IOLoop
## getting blocked (often indicated by your upstream HTTP requests timing out)
## Defaults to: 0
{{- with .Env.ENGINE_THREADPOOL_SIZE }}
ENGINE_THREADPOOL_SIZE = {{ atoi . }}
{{- end }}

################################################################################


################################ Extensibility #################################

## The metrics backend thumbor should use to measure internal actions. This must
## be the full name of a python module (python must be able to import it)
## Defaults to: 'thumbor.metrics.logger_metrics'
{{- with .Env.METRICS }}
METRICS = '{{ . }}'
{{- end }}

## The loader thumbor should use to load the original image. This must be the
## full name of a python module (python must be able to import it)
## Defaults to: 'thumbor.loaders.http_loader'
{{- with .Env.LOADER }}
LOADER = '{{ . }}'
{{- end }}

## The file storage thumbor should use to store original images. This must be the
## full name of a python module (python must be able to import it)
## Defaults to: 'thumbor.storages.file_storage'
{{- with .Env.STORAGE }}
STORAGE = '{{ . }}'
{{- end }}

## The result storage thumbor should use to store generated images. This must be
## the full name of a python module (python must be able to import it)
## Defaults to: None
{{- with .Env.RESULT_STORAGE }}
RESULT_STORAGE = '{{ . }}'
{{- end }}

## The imaging engine thumbor should use to perform image operations. This must
## be the full name of a python module (python must be able to import it)
## Defaults to: 'thumbor.engines.pil'
{{- with .Env.ENGINE }}
ENGINE = '{{ . }}'
{{- end }}

## The gif engine thumbor should use to perform image operations. This must be
## the full name of a python module (python must be able to import it)
## Defaults to: 'thumbor.engines.gif'
{{- with .Env.GIF_ENGINE }}
GIF_ENGINE = '{{ . }}'
{{- end }}

## The url signer thumbor should use to verify url signatures.This must be the
## full name of a python module (python must be able to import it)
## Defaults to: 'libthumbor.url_signers.base64_hmac_sha1'
{{- with .Env.URL_SIGNER }}
URL_SIGNER = '{{ . }}'
{{- end }}

################################################################################


################################### Security ###################################

## The security key thumbor uses to sign image URLs
## Defaults to: 'MY_SECURE_KEY'
{{- with .Env.SECURITY_KEY }}
SECURITY_KEY = '{{ . }}'
{{- end }}

## Indicates if the /unsafe URL should be available
## Defaults to: True
{{- with .Env.ALLOW_UNSAFE_URL }}
ALLOW_UNSAFE_URL = {{ if isTrue . }}True{{ else }}False{{- end }}
{{- end }}

## Indicates if encrypted (old style) URLs should be allowed
## Defaults to: True
{{- with .Env.ALLOW_OLD_URLS }}
ALLOW_OLD_URLS = {{ if isTrue . }}True{{ else }}False{{- end }}
{{- end }}

################################################################################


##################################### HTTP #####################################

## Enables automatically generated etags
## Defaults to: True
{{- with .Env.ENABLE_ETAGS }}
ENABLE_ETAGS = {{ if isTrue . }}True{{ else }}False{{- end }}
{{- end }}

################################################################################


################################### Storage ####################################

## Set maximum id length for images when stored
## Defaults to: 32
{{- with .Env.MAX_ID_LENGTH }}
MAX_ID_LENGTH = {{ atoi . }}
{{- end }}

################################################################################


################################# Performance ##################################

## Set garbage collection interval in seconds
## Defaults to: None
{{- with .Env.GC_INTERVAL }}
GC_INTERVAL = {{ atoi . }}
{{- end }}

################################################################################


################################### Metrics ####################################

## Host to send statsd instrumentation to
## Defaults to: None
{{- with .Env.STATSD_HOST }}
STATSD_HOST = '{{ . }}'
{{- end }}

## Port to send statsd instrumentation to
## Defaults to: 8125
{{- with .Env.STATSD_PORT }}
STATSD_PORT = {{ atoi . }}
{{- end }}

## Prefix for statsd
## Defaults to: None
{{- with .Env.STATSD_PREFIX }}
STATSD_PREFIX = '{{ . }}'
{{- end }}

################################################################################


################################# File Loader ##################################

## The root path where the File Loader will try to find images
## Defaults to: '/root'
{{- with .Env.FILE_LOADER_ROOT_PATH }}
FILE_LOADER_ROOT_PATH = '{{ . }}'
{{- end }}

################################################################################


################################# HTTP Loader ##################################

## The maximum number of seconds libcurl can take to connect to an image being
## loaded
## Defaults to: 5
{{- with .Env.HTTP_LOADER_CONNECT_TIMEOUT }}
HTTP_LOADER_CONNECT_TIMEOUT = {{ atoi . }}
{{- end }}

## The maximum number of seconds libcurl can take to download an image
## Defaults to: 20
{{- with .Env.HTTP_LOADER_REQUEST_TIMEOUT }}
HTTP_LOADER_REQUEST_TIMEOUT = {{ atoi . }}
{{- end }}

## Indicates whether libcurl should follow redirects when downloading an image
## Defaults to: True
{{- with .Env.HTTP_LOADER_FOLLOW_REDIRECTS }}
HTTP_LOADER_FOLLOW_REDIRECTS = {{ if isTrue . }}True{{ else }}False{{- end }}
{{- end }}

## Indicates the number of redirects libcurl should follow when downloading an
## image
## Defaults to: 5
{{- with .Env.HTTP_LOADER_MAX_REDIRECTS }}
HTTP_LOADER_MAX_REDIRECTS = {{ atoi . }}
{{- end }}

## The maximum number of simultaneous HTTP connections the loader can make before
## queuing
## Defaults to: 10
{{- with .Env.HTTP_LOADER_MAX_CLIENTS }}
HTTP_LOADER_MAX_CLIENTS = {{ atoi . }}
{{- end }}

## Indicates whether thumbor should forward the user agent of the requesting user
## Defaults to: False
{{- with .Env.HTTP_LOADER_FORWARD_USER_AGENT }}
HTTP_LOADER_FORWARD_USER_AGENT = {{ if isTrue . }}True{{ else }}False{{- end }}
{{- end }}

## Indicates whether thumbor should forward the headers of the request
## Defaults to: False
{{- with .Env.HTTP_LOADER_FORWARD_ALL_HEADERS }}
HTTP_LOADER_FORWARD_ALL_HEADERS = {{ if isTrue . }}True{{ else }}False{{- end }}
{{- end }}

## Indicates which headers should be forwarded among all the headers of the
## request
## Defaults to: #    [
#    ]
{{- with .Env.HTTP_LOADER_FORWARD_HEADERS_WHITELIST }}
HTTP_LOADER_FORWARD_HEADERS_WHITELIST = [
{{- range $value := (split . " ") }}
    "{{ $value }}",
{{- end }}
]
{{- end }}


## Default user agent for thumbor http loader requests
## Defaults to: 'Thumbor/6.6.0'
{{- with .Env.HTTP_LOADER_DEFAULT_USER_AGENT }}
HTTP_LOADER_DEFAULT_USER_AGENT = '{{ . }}'
{{- end }}

## The proxy host needed to load images through
## Defaults to: None
{{- with .Env.HTTP_LOADER_PROXY_HOST }}
HTTP_LOADER_PROXY_HOST = '{{ . }}'
{{- end }}

## The proxy port for the proxy host
## Defaults to: None
{{- with .Env.HTTP_LOADER_PROXY_PORT }}
HTTP_LOADER_PROXY_PORT = {{ atoi . }}
{{- end }}

## The proxy username for the proxy host
## Defaults to: None
{{- with .Env.HTTP_LOADER_PROXY_USERNAME }}
HTTP_LOADER_PROXY_USERNAME = '{{ . }}'
{{- end }}

## The proxy password for the proxy host
## Defaults to: None
{{- with .Env.HTTP_LOADER_PROXY_PASSWORD }}
HTTP_LOADER_PROXY_PASSWORD = '{{ . }}'
{{- end }}

## The filename of CA certificates in PEM format
## Defaults to: None
{{- with .Env.HTTP_LOADER_CA_CERTS }}
HTTP_LOADER_CA_CERTS = '{{ . }}'
{{- end }}

## Validate the server’s certificate for HTTPS requests
## Defaults to: None
{{- with .Env.HTTP_LOADER_VALIDATE_CERTS }}
HTTP_LOADER_VALIDATE_CERTS = '{{ . }}'
{{- end }}

## The filename for client SSL key
## Defaults to: None
{{- with .Env.HTTP_LOADER_CLIENT_KEY }}
HTTP_LOADER_CLIENT_KEY = '{{ . }}'
{{- end }}

## The filename for client SSL certificate
## Defaults to: None
{{- with .Env.HTTP_LOADER_CLIENT_CERT }}
HTTP_LOADER_CLIENT_CERT = '{{ . }}'
{{- end }}

## If the CurlAsyncHTTPClient should be used
## Defaults to: False
{{- with .Env.HTTP_LOADER_CURL_ASYNC_HTTP_CLIENT }}
HTTP_LOADER_CURL_ASYNC_HTTP_CLIENT = {{ if isTrue . }}True{{ else }}False{{- end }}
{{- end }}

################################################################################


################################### General ####################################

## If HTTP_LOADER_CURL_LOW_SPEED_LIMIT and HTTP_LOADER_CURL_ASYNC_HTTP_CLIENT are
## set, then this is the time in seconds as integer after a download should
## timeout if the speed is below HTTP_LOADER_CURL_LOW_SPEED_LIMIT for that
## long
## Defaults to: 0
{{- with .Env.HTTP_LOADER_CURL_LOW_SPEED_TIME }}
HTTP_LOADER_CURL_LOW_SPEED_TIME = {{ atoi . }}
{{- end }}

## If HTTP_LOADER_CURL_LOW_SPEED_TIME and HTTP_LOADER_CURL_ASYNC_HTTP_CLIENT are
## set, then this is the limit in bytes per second as integer which should
## timeout if the speed is below that limit for
## HTTP_LOADER_CURL_LOW_SPEED_TIME seconds
## Defaults to: 0
{{- with .Env.HTTP_LOADER_CURL_LOW_SPEED_LIMIT }}
HTTP_LOADER_CURL_LOW_SPEED_LIMIT = {{ atoi . }}
{{- end }}

## Custom app class to override ThumborServiceApp. This config value is
## overridden by the -a command-line parameter.
## Defaults to: 'thumbor.app.ThumborServiceApp'
{{- with .Env.APP_CLASS }}
APP_CLASS = '{{ . }}'
{{- end }}

################################################################################


################################# File Storage #################################

## Expiration in seconds for the images in the File Storage. Defaults to one
## month
## Defaults to: 2592000
{{- with .Env.STORAGE_EXPIRATION_SECONDS }}
STORAGE_EXPIRATION_SECONDS = {{ atoi . }}
{{- end }}

## Indicates whether thumbor should store the signing key for each image in the
## file storage. This allows the key to be changed and old images to still be
## properly found
## Defaults to: False
{{- with .Env.STORES_CRYPTO_KEY_FOR_EACH_IMAGE }}
STORES_CRYPTO_KEY_FOR_EACH_IMAGE = {{ if isTrue . }}True{{ else }}False{{- end }}
{{- end }}

## The root path where the File Storage will try to find images
## Defaults to: '/tmp/thumbor/storage'
{{- with .Env.FILE_STORAGE_ROOT_PATH }}
FILE_STORAGE_ROOT_PATH = '{{ . }}'
{{- end }}

################################################################################


#################################### Upload ####################################

## Max size in Kb for images uploaded to thumbor
## Aliases: MAX_SIZE
## Defaults to: 0
{{- with .Env.UPLOAD_MAX_SIZE }}
UPLOAD_MAX_SIZE = {{ atoi . }}
{{- end }}

## Indicates whether thumbor should enable File uploads
## Aliases: ENABLE_ORIGINAL_PHOTO_UPLOAD
## Defaults to: False
{{- with .Env.UPLOAD_ENABLED }}
UPLOAD_ENABLED = {{ if isTrue . }}True{{ else }}False{{- end }}
{{- end }}

## The type of storage to store uploaded images with
## Aliases: ORIGINAL_PHOTO_STORAGE
## Defaults to: 'thumbor.storages.file_storage'
{{- with .Env.UPLOAD_PHOTO_STORAGE }}
UPLOAD_PHOTO_STORAGE = '{{ . }}'
{{- end }}

## Indicates whether image deletion should be allowed
## Aliases: ALLOW_ORIGINAL_PHOTO_DELETION
## Defaults to: False
{{- with .Env.UPLOAD_DELETE_ALLOWED }}
UPLOAD_DELETE_ALLOWED = {{ if isTrue . }}True{{ else }}False{{- end }}
{{- end }}

## Indicates whether image overwrite should be allowed
## Aliases: ALLOW_ORIGINAL_PHOTO_PUTTING
## Defaults to: False
{{- with .Env.UPLOAD_PUT_ALLOWED }}
UPLOAD_PUT_ALLOWED = {{ if isTrue . }}True{{ else }}False{{- end }}
{{- end }}

## Default filename for image uploaded
## Defaults to: 'image'
{{- with .Env.UPLOAD_DEFAULT_FILENAME }}
UPLOAD_DEFAULT_FILENAME = '{{ . }}'
{{- end }}

################################################################################


############################### Memcache Storage ###############################

## List of Memcache storage server hosts
## Defaults to: #    [
#        'localhost:11211',
#    ]
{{- with .Env.MEMCACHE_STORAGE_SERVERS }}
MEMCACHE_STORAGE_SERVERS = [
{{- range $value := (split . " ") }}
    "{{ $value }}",
{{- end }}
]
{{- end }}


################################################################################


################################ Mixed Storage #################################

## Mixed Storage file storage. This must be the full name of a python module
## (python must be able to import it)
## Defaults to: 'thumbor.storages.no_storage'
{{- with .Env.MIXED_STORAGE_FILE_STORAGE }}
MIXED_STORAGE_FILE_STORAGE = '{{ . }}'
{{- end }}

## Mixed Storage signing key storage. This must be the full name of a python
## module (python must be able to import it)
## Defaults to: 'thumbor.storages.no_storage'
{{- with .Env.MIXED_STORAGE_CRYPTO_STORAGE }}
MIXED_STORAGE_CRYPTO_STORAGE = '{{ . }}'
{{- end }}

## Mixed Storage detector information storage. This must be the full name of a
## python module (python must be able to import it)
## Defaults to: 'thumbor.storages.no_storage'
{{- with .Env.MIXED_STORAGE_DETECTOR_STORAGE }}
MIXED_STORAGE_DETECTOR_STORAGE = '{{ . }}'
{{- end }}

################################################################################


##################################### Meta #####################################

## The callback function name that should be used by the META route for JSONP
## access
## Defaults to: None
{{- with .Env.META_CALLBACK_NAME }}
META_CALLBACK_NAME = '{{ . }}'
{{- end }}

################################################################################


################################## Detection ###################################

## List of detectors that thumbor should use to find faces and/or features. All
## of them must be full names of python modules (python must be able to import
## it)
## Defaults to: #    [
#    ]
{{- with .Env.DETECTORS }}
DETECTORS = [
{{- range $value := (split . " ") }}
    "{{ $value }}",
{{- end }}
]
{{- end }}


## The cascade file that opencv will use to detect faces.
## Defaults to: 'haarcascade_frontalface_alt.xml'
{{- with .Env.FACE_DETECTOR_CASCADE_FILE }}
FACE_DETECTOR_CASCADE_FILE = '{{ . }}'
{{- end }}

## The cascade file that opencv will use to detect glasses.
## Defaults to: 'haarcascade_eye_tree_eyeglasses.xml'
{{- with .Env.GLASSES_DETECTOR_CASCADE_FILE }}
GLASSES_DETECTOR_CASCADE_FILE = '{{ . }}'
{{- end }}

## The cascade file that opencv will use to detect profile faces.
## Defaults to: 'haarcascade_profileface.xml'
{{- with .Env.PROFILE_DETECTOR_CASCADE_FILE }}
PROFILE_DETECTOR_CASCADE_FILE = '{{ . }}'
{{- end }}

################################################################################


################################## Optimizers ##################################

## List of optimizers that thumbor will use to optimize images
## Defaults to: #    [
#    ]
{{- with .Env.OPTIMIZERS }}
OPTIMIZERS = [
{{- range $value := (split . " ") }}
    "{{ $value }}",
{{- end }}
]
{{- end }}


## Path for the jpegtran binary
## Defaults to: '/usr/bin/jpegtran'
{{- with .Env.JPEGTRAN_PATH }}
JPEGTRAN_PATH = '{{ . }}'
{{- end }}

## Path for the progressive scans file to use with jpegtran optimizer. Implies
## progressive jpeg output
## Defaults to: ''
{{- with .Env.JPEGTRAN_SCANS_FILE }}
JPEGTRAN_SCANS_FILE = '{{ . }}'
{{- end }}

## Path for the ffmpeg binary used to generate gifv(h.264)
## Defaults to: '/usr/local/bin/ffmpeg'
{{- with .Env.FFMPEG_PATH }}
FFMPEG_PATH = '{{ . }}'
{{- end }}

################################################################################


################################### Filters ####################################

## List of filters that thumbor will allow to be used in generated images. All of
## them must be full names of python modules (python must be able to import
## it)
## Defaults to: #    [
#        'thumbor.filters.brightness',
#        'thumbor.filters.colorize',
#        'thumbor.filters.contrast',
#        'thumbor.filters.rgb',
#        'thumbor.filters.round_corner',
#        'thumbor.filters.quality',
#        'thumbor.filters.noise',
#        'thumbor.filters.watermark',
#        'thumbor.filters.equalize',
#        'thumbor.filters.fill',
#        'thumbor.filters.sharpen',
#        'thumbor.filters.strip_exif',
#        'thumbor.filters.strip_icc',
#        'thumbor.filters.frame',
#        'thumbor.filters.grayscale',
#        'thumbor.filters.rotate',
#        'thumbor.filters.format',
#        'thumbor.filters.max_bytes',
#        'thumbor.filters.convolution',
#        'thumbor.filters.blur',
#        'thumbor.filters.extract_focal',
#        'thumbor.filters.focal',
#        'thumbor.filters.no_upscale',
#        'thumbor.filters.saturation',
#        'thumbor.filters.max_age',
#        'thumbor.filters.curve',
#        'thumbor.filters.background_color',
#        'thumbor.filters.upscale',
#        'thumbor.filters.proportion',
#        'thumbor.filters.stretch',
#    ]
{{- with .Env.FILTERS }}
FILTERS = [
{{- range $value := (split . " ") }}
    '{{ $value }}',
{{- end }}
]
{{- end }}


################################################################################


################################ Result Storage ################################

## Expiration in seconds of generated images in the result storage
## Defaults to: 0
{{- with .Env.RESULT_STORAGE_EXPIRATION_SECONDS }}
RESULT_STORAGE_EXPIRATION_SECONDS = {{ atoi . }}
{{- end }}

## Path where the Result storage will store generated images
## Defaults to: '/tmp/thumbor/result_storage'
{{- with .Env.RESULT_STORAGE_FILE_STORAGE_ROOT_PATH }}
RESULT_STORAGE_FILE_STORAGE_ROOT_PATH = '{{ . }}'
{{- end }}

## Indicates whether unsafe requests should also be stored in the Result Storage
## Defaults to: False
{{- with .Env.RESULT_STORAGE_STORES_UNSAFE }}
RESULT_STORAGE_STORES_UNSAFE = {{ if isTrue . }}True{{ else }}False{{- end }}
{{- end }}

################################################################################


############################ Queued Redis Detector #############################

## Server host for the queued redis detector
## Defaults to: 'localhost'
{{- with .Env.REDIS_QUEUE_SERVER_HOST }}
REDIS_QUEUE_SERVER_HOST = '{{ . }}'
{{- end }}

## Server port for the queued redis detector
## Defaults to: 6379
{{- with .Env.REDIS_QUEUE_SERVER_PORT }}
REDIS_QUEUE_SERVER_PORT = {{ atoi . }}
{{- end }}

## Server database index for the queued redis detector
## Defaults to: 0
{{- with .Env.REDIS_QUEUE_SERVER_DB }}
REDIS_QUEUE_SERVER_DB = {{ atoi . }}
{{- end }}

## Server password for the queued redis detector
## Defaults to: None
{{- with .Env.REDIS_QUEUE_SERVER_PASSWORD }}
REDIS_QUEUE_SERVER_PASSWORD = '{{ . }}'
{{- end }}

################################################################################


############################# Queued SQS Detector ##############################

## AWS key id
## Defaults to: None
{{- with .Env.SQS_QUEUE_KEY_ID }}
SQS_QUEUE_KEY_ID = '{{ . }}'
{{- end }}

## AWS key secret
## Defaults to: None
{{- with .Env.SQS_QUEUE_KEY_SECRET }}
SQS_QUEUE_KEY_SECRET = '{{ . }}'
{{- end }}

## AWS SQS region
## Defaults to: 'us-east-1'
{{- with .Env.SQS_QUEUE_REGION }}
SQS_QUEUE_REGION = '{{ . }}'
{{- end }}

################################################################################


#################################### Errors ####################################

## This configuration indicates whether thumbor should use a custom error
## handler.
## Defaults to: False
{{- with .Env.USE_CUSTOM_ERROR_HANDLING }}
USE_CUSTOM_ERROR_HANDLING = {{ if isTrue . }}True{{ else }}False{{- end }}
{{- end }}

## Error reporting module. Needs to contain a class called ErrorHandler with a
## handle_error(context, handler, exception) method.
## Defaults to: 'thumbor.error_handlers.sentry'
{{- with .Env.ERROR_HANDLER_MODULE }}
ERROR_HANDLER_MODULE = '{{ . }}'
{{- end }}

## File of error log as json
## Defaults to: None
{{- with .Env.ERROR_FILE_LOGGER }}
ERROR_FILE_LOGGER = '{{ . }}'
{{- end }}

## File of error log name is parametrized with context attribute
## Defaults to: False
{{- with .Env.ERROR_FILE_NAME_USE_CONTEXT }}
ERROR_FILE_NAME_USE_CONTEXT = {{ if isTrue . }}True{{ else }}False{{- end }}
{{- end }}

################################################################################


############################### Errors - Sentry ################################

## Sentry thumbor project dsn. i.e.: http://5a63d58ae7b94f1dab3dee740b301d6a:73ee
## a45d3e8649239a973087e8f21f98@localhost:9000/2
## Defaults to: ''
{{- with .Env.SENTRY_DSN_URL }}
SENTRY_DSN_URL = '{{ . }}'
{{- end }}

################################################################################


#################################### Server ####################################

## The amount of time to wait before shutting down the server, i.e. stop
## accepting requests.
## Defaults to: 0
{{- with .Env.MAX_WAIT_SECONDS_BEFORE_SERVER_SHUTDOWN }}
MAX_WAIT_SECONDS_BEFORE_SERVER_SHUTDOWN = {{ atoi . }}
{{- end }}

## The amount of time to waut before shutting down all io, after the server has
## been stopped
## Defaults to: 0
{{- with .Env.MAX_WAIT_SECONDS_BEFORE_IO_SHUTDOWN }}
MAX_WAIT_SECONDS_BEFORE_IO_SHUTDOWN = {{ atoi . }}
{{- end }}

################################################################################

################################ Storage - Redis ###############################

# Defaults to: True
{{- with .Env.REDIS_STORAGE_IGNORE_ERRORS }}
REDIS_STORAGE_IGNORE_ERRORS = {{ if isTrue . }}True{{ else }}False{{- end }}
{{- end }}

# Defaults to: 6379
REDIS_STORAGE_SERVER_PORT = {{ atoi (default .Env.REDIS_STORAGE_SERVER_PORT "6379") }}

# Defaults to: localhost
REDIS_STORAGE_SERVER_HOST = '{{ default .Env.REDIS_STORAGE_SERVER_HOST "localhost" }}'

# Defaults to: 0
REDIS_STORAGE_SERVER_DB = {{ atoi (default .Env.REDIS_STORAGE_SERVER_DB "0") }}

# Defaults to: None
REDIS_STORAGE_SERVER_PASSWORD = None
{{- with .Env.REDIS_STORAGE_SERVER_PASSWORD }}
REDIS_STORAGE_SERVER_PASSWORD = '{{ . }}'
{{- end }}


################################################################################


################################ Result Storage - Redis ########################

# Defaults to: True
{{- with .Env.REDIS_RESULT_STORAGE_IGNORE_ERRORS }}
REDIS_RESULT_STORAGE_IGNORE_ERRORS = {{ if isTrue . }}True{{ else }}False{{- end }}
{{- end }}

# Defaults to: 6379
REDIS_RESULT_STORAGE_SERVER_PORT = {{ atoi (default .Env.REDIS_RESULT_STORAGE_SERVER_PORT "6379") }}

# Defaults to: localhost
REDIS_RESULT_STORAGE_SERVER_HOST = '{{ default .Env.REDIS_RESULT_STORAGE_SERVER_HOST "localhost" }}'

# Defaults to: 0
REDIS_RESULT_STORAGE_SERVER_DB = {{ atoi (default .Env.REDIS_RESULT_STORAGE_SERVER_DB "0") }}

# Defaults to: None
REDIS_RESULT_STORAGE_SERVER_PASSWORD = None
{{- with .Env.REDIS_RESULT_STORAGE_SERVER_PASSWORD }}
REDIS_RESULT_STORAGE_SERVER_PASSWORD = '{{ . }}'
{{- end }}

################################################################################


################################ Storage - Memcached ###############################

# List of memcached servers to use for keys
# Defaults to: localhost:55555
{{- with .Env.MEMCACHE_STORAGE_SERVERS }}
MEMCACHE_STORAGE_SERVERS = [
{{- range $value := (split . " ") }}
    '{{ $value }}',
{{- end }}
]
{{- end }}

# Expiration of entries in the memcached storage
# Defaults to: 120
{{- with .Env.STORAGE_EXPIRATION_SECONDS }}
STORAGE_EXPIRATION_SECONDS = {{ atoi . }}
{{- end }}

################################################################################


################################ Result Storage - Memcached ########################

# Defaults to: 1024 * 1024 (bytes. Default of item_size_max)
{{- with .Env.MEMCACHE_ITEM_SIZE_MAX }}
MEMCACHE_ITEM_SIZE_MAX = {{ atoi . }}
{{- end }}

# Not skipping can throw TooBig error
# Defaults to: False
{{- with .Env.MEMCACHE_SKIP_STORAGE_EXCEEDING_ITEM_SIZE_MAX }}
MEMCACHE_SKIP_STORAGE_EXCEEDING_ITEM_SIZE_MAX = {{ if isTrue . }}True{{ else }}False{{- end }}
{{- end }}

# Defaults to: 120
{{- with .Env.RESULT_STORAGE_EXPIRATION_SECONDS }}
RESULT_STORAGE_EXPIRATION_SECONDS = {{ atoi . }}
{{- end }}

# Defaults to: True
{{- with .Env.RESULT_STORAGE_STORES_UNSAFE }}
RESULT_STORAGE_STORES_UNSAFE = {{ if isTrue . }}True{{ else }}False{{- end }}
{{- end }}

################################################################################


################################ Storage - Mongo ###############################

# MongoDB storage server host
# Defaults to: localhost
{{- with .Env.MONGO_STORAGE_SERVER_HOST }}
MONGO_STORAGE_SERVER_HOST = '{{ . }}'
{{- end }}

# MongoDB storage server port
# Defaults to: 27017
{{- with .Env.MONGO_STORAGE_SERVER_PORT }}
MONGO_STORAGE_SERVER_PORT = {{ atoi . }}
{{- end }}

# MongoDB storage server database name
# Defaults to: thumbor
{{- with .Env.MONGO_STORAGE_SERVER_DB }}
MONGO_STORAGE_SERVER_DB = '{{ . }}'
{{- end }}

# MongoDB storage image collection
# Defaults to: images
{{- with .Env.MONGO_STORAGE_SERVER_COLLECTION }}
MONGO_STORAGE_SERVER_COLLECTION = '{{ . }}'
{{- end }}

################################################################################


################################ Result Storage - Mongo ########################


################################################################################
