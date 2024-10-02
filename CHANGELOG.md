# OO Patterns Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.7.0] - 2024-10-02
### Added
- Implement `init_state` functionality for `state` OO pattern. See `oo_patterns/behavioral/state/` directory for details.

## [0.6.0] - 2024-09-14

### Added
- Implement `BaseSubSpacePublisher`/`BaseAsyncSubSpacePublisher` with supporting subscribing on events sub-spaces. See `oo_patterns/behavioral/observer/sub_space_publishers.py` file for details.

### Changed
- Implement returning errors from `notify_subscribers` of `Observer` classes. See `oo_patterns/behavioral/observer/` directory for details.

### Deleted
- Methods `handle_subscriber_error` are deleted from `Observer` classes. See `oo_patterns/behavioral/observer/` directory for details.

## [0.5.0] - 2024-07-27

### Added
- Implement `TestingMixin` helper for unifying testing processes. See `oo_patterns/tests/helpers.py` file for details.
- Add `remove_all_subscribers` method into `Observer` classes. See `oo_patterns/behavioral/observer/` directory for details.

## [0.4.0] - 2024-07-21

### Added
- Implement Observer behavioral programming pattern. See `oo_patterns/behavioral/observer/` directory for details.

## [0.3.0] - 2024-07-20

### Changed
- Rename root package directory. Use `oo_patterns` for importing instead `oop`.
- Change package PyPI name. The `ak-` prefix is added. It's `ak-oo-patterns` now instead `oop`.

## [0.2.0] - 2024-06-10

### Added
- Implement State behavioral programming pattern. See `oo_patterns/behavioral/state/` directory for details.

## [0.1.0] - 2024-06-09

### Added
- Generate package structure. See the root directory for details.
