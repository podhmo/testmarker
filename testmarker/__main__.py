from unittest.main import TestProgram


class WithMarkerTestProgram(TestProgram):
    def _getDiscoveryArgParser(self, parent):
        parser = super()._getDiscoveryArgParser(parent)
        parser.add_argument("--only", action="append")
        parser.add_argument("--ignore", action="append")
        return parser

    def get_markers(self):
        from testmarker import mark
        return mark

    def _do_discovery(self, argv, Loader=None):
        args = self._discovery_parser.parse_args()
        markers = self.get_markers()
        if args.only is not None:
            markers.only(args.only, skip_unmarked=True)
        elif args.ignore is not None:
            markers.ignore(args.only)
        if args.start is None:
            args.start = "discover"
        return super()._do_discovery(argv, Loader=Loader)


__unittest = True
WithMarkerTestProgram(module=None)
