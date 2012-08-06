<%inherit file="layout.tpl"/>
<%block name="page_includes">
<style>
#feedback { font-size: 1.4em; }
#selectable .ui-selecting { background: #FECA40; }
#selectable .ui-selected { background: #F39814; color: white; }
#selectable { list-style-type: none; margin: 0; padding: 0; width: 60%; }
#selectable li { margin: 3px; padding: 0.4em; font-size: 1.4em; height: 18px; }
</style>
<script>
</script>
</%block>
<%block name="content">
<div id="track-locations-map">
<div id="map_canvas" style="width:250px;height:250px"></div>
<script type="text/javascript">
        $(function() {
                var yourStartLatLng = new google.maps.LatLng(42.333796,-71.051582);
                $('#map_canvas').gmap({'center': yourStartLatLng});
        });
</script>
                % for row in data_grid:
                ${loop.index}: ${row} <br />
                //$('#map_canvas').gmap('addMarker', { /*id:'m_${loop.index}',*/ 'position': '42.345573,-71.098326', 'bounds': true } );
                % endfor
</div>
<p />
<div id="track-locations-grid">
    <p> ${ data_grid_string.replace('\n', '<br />\n') } </p>
</div>
</%block>
